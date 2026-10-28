"""Exercise failure cases and the portable ZIP's distribution boundary."""

from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from package import build_package
from validate import NAME, validate


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / NAME
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(
            ".git", ".venv", "__pycache__", "dist"))

    def test_repository_validates(self):
        validate(self.root)

    def test_missing_reference_is_rejected(self):
        (self.root / "references/action-controls.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing or external local link"):
            validate(self.root)

    def test_local_link_cannot_escape_repository(self):
        readme = self.root / "README.md"
        readme.write_text("[outside](../../outside.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Missing or external local link"):
            validate(self.root)

    def test_game_binary_is_rejected(self):
        (self.root / "original.exe").write_bytes(b"MZ")
        with self.assertRaisesRegex(ValueError, "Do not publish game packages"):
            validate(self.root)

    def test_credentials_are_rejected(self):
        (self.root / ".env.local").write_text("EXAMPLE=value\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Do not publish game packages"):
            validate(self.root)

    def test_zip_is_complete_and_excludes_gallery_and_development_files(self):
        output = build_package(self.root, self.root / "dist/skill.zip")
        with zipfile.ZipFile(output) as archive:
            expected = {f"{NAME}/{path}" for path in (
                "SKILL.md", "LICENSE", "agents/openai.yaml")}
            expected.update(f"{NAME}/{path.relative_to(self.root)}"
                            for path in (self.root / "references").glob("*.md"))
            self.assertEqual(set(archive.namelist()), expected)
            self.assertIsNone(archive.testzip())
            extracted = Path(self.temporary.name) / "extracted"
            archive.extractall(extracted)
        validate(extracted / NAME)


if __name__ == "__main__":
    unittest.main()
