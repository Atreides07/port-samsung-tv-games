#!/usr/bin/env python3
"""Check this skill's metadata, local links, and publication hygiene."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = "port-samsung-tv-games"
IGNORED = {".git", ".venv", "__pycache__", "dist"}


def validate(root):
    root = root.resolve()
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError("SKILL.md needs YAML frontmatter")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict) or metadata.get("name") != NAME:
        raise ValueError("Skill name must match the published directory name")
    description = metadata.get("description")
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        raise ValueError("Description must contain 1–1024 characters")
    if metadata.get("license") != "MIT" or not (root / "LICENSE").is_file():
        raise ValueError("The skill must include its declared MIT license")

    ui = yaml.safe_load((root / "agents/openai.yaml").read_text(encoding="utf-8"))
    interface = ui["interface"]
    if not 25 <= len(interface["short_description"]) <= 64:
        raise ValueError("UI short_description must contain 25–64 characters")
    if f"${NAME}" not in interface["default_prompt"]:
        raise ValueError("Default prompt must invoke the skill")
    if ui.get("policy", {}).get("allow_implicit_invocation") is not True:
        raise ValueError("Preserve automatic skill discovery")

    forbidden = {".exe", ".com", ".rar", ".zip", ".wgt", ".p12", ".pfx", ".pem"}
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in IGNORED for part in relative.parts):
            continue
        if path.is_symlink():
            raise ValueError(f"Do not publish symlinks: {relative}")
        if not path.is_file():
            continue
        if path.suffix.lower() in forbidden or path.name.startswith(".env"):
            raise ValueError(f"Do not publish game packages or credentials: {relative}")
        if path.suffix != ".md":
            continue
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)\s]+)\)", content):
            url = urlsplit(target)
            if url.scheme or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.is_file():
                raise ValueError(f"Missing or external local link in {relative}: {target}")


if __name__ == "__main__":
    try:
        validate(ROOT)
    except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
    print("Skill metadata, local links, and publication hygiene checks passed.")
