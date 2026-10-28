#!/usr/bin/env python3
"""Build the portable instruction-only skill ZIP for account uploads."""

from pathlib import Path
import zipfile

from validate import NAME, ROOT, validate


def build_package(root, output):
    validate(root)
    files = [root / "SKILL.md", root / "LICENSE", root / "agents/openai.yaml"]
    files.extend(sorted((root / "references").rglob("*.md")))
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".tmp")
    try:
        with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in files:
                archive.write(path, Path(NAME) / path.relative_to(root))
        with zipfile.ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise ValueError("Generated ZIP failed its integrity check")
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    return output


if __name__ == "__main__":
    output = build_package(ROOT, ROOT / "dist" / f"{NAME}.zip")
    print(f"{output} ({output.stat().st_size:,} bytes)")
