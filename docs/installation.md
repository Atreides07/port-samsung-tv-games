# Installation

The repository is one portable Agent Skill. Install the complete skill folder,
including `references/`; copying only SKILL.md loses conditional guidance.
No API key, MCP server, or TV connection is required to install the instructions.

Choose one location per agent to avoid duplicate same-named skills. Git commands
below create a new folder and stop if it already exists; they do not overwrite an
existing installation. For an existing copy, see [Updates](#updates).

## Codex

For a personal installation on macOS/Linux:

```sh
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/Atreides07/port-samsung-tv-games.git \
  "$HOME/.agents/skills/port-samsung-tv-games"
```

For a project installation, run from the game repository root instead:

```sh
mkdir -p .agents/skills
git clone https://github.com/Atreides07/port-samsung-tv-games.git \
  .agents/skills/port-samsung-tv-games
```

Invoke with `$port-samsung-tv-games` in Codex, or select it in the skill picker.
If it does not appear, open a new session or restart the client. This repository
includes optional `agents/openai.yaml` metadata and keeps automatic invocation
enabled. Follow your installed client's configured skill location if it differs;
do not create a second copy simply because an older setup uses `~/.codex/skills`.
[Official Codex skill locations and invocation](https://learn.chatgpt.com/docs/build-skills?kbid=111697).

## Claude Code

Personal installation on macOS/Linux:

```sh
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/Atreides07/port-samsung-tv-games.git \
  "$HOME/.claude/skills/port-samsung-tv-games"
```

For a project, use `.claude/skills/port-samsung-tv-games/` instead. Invoke
`/port-samsung-tv-games` in Claude Code, then describe the game or focused fix.
The standard SKILL.md and references carry the workflow; Codex-specific UI
metadata is not required by other agents.
[Official Claude Code skills guide](https://code.claude.com/docs/en/skills).

## Cursor

Personal installation on macOS/Linux:

```sh
mkdir -p "$HOME/.cursor/skills"
git clone https://github.com/Atreides07/port-samsung-tv-games.git \
  "$HOME/.cursor/skills/port-samsung-tv-games"
```

Use `.cursor/skills/port-samsung-tv-games/` for a project installation. Select the
skill through `/` in Agent chat, or ask Agent to use it. Cursor also recognizes
`.agents/skills/`, so an existing shared project installation can be reused.
Personal local files do not automatically become available to remote agents.
[Official Cursor skills guide](https://cursor.com/docs/skills).

## Windows PowerShell

Choose the personal root for your agent, then clone:

```powershell
# Codex; use .claude\skills for Claude Code or .cursor\skills for Cursor.
$skillRoot = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
git clone https://github.com/Atreides07/port-samsung-tv-games.git `
  (Join-Path $skillRoot 'port-samsung-tv-games')
```

This assumes Git is installed and available in the terminal. For a project copy,
use the matching relative skills directory in the repository instead.

## Claude web / Desktop account skills

Download [port-samsung-tv-games.zip from the latest release](https://github.com/Atreides07/port-samsung-tv-games/releases/latest/download/port-samsung-tv-games.zip),
or build the upload ZIP from a repository checkout:

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/package.py
```

The result is `dist/port-samsung-tv-games.zip`. Its layout is:

```text
port-samsung-tv-games.zip
└── port-samsung-tv-games/
    ├── SKILL.md
    ├── LICENSE
    ├── agents/openai.yaml
    └── references/...
```

Enable code execution/file creation as required by your account, then open
**Customize → Skills → + → Create skill → Upload a skill**, upload the ZIP, and
enable it. Menu labels and organization policy can vary.
[Official upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude),
[ZIP structure](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

A cloud account skill provides instructions. It does not grant access to your
local game files, signing keys, SDK, or television. Local hardware work requires
an appropriately connected environment. Local Claude Code installation and an
account upload are separate distribution paths.

## Check discovery

Ask your agent:

```text
Use the Samsung TV Game Ports skill. Before changing files, tell me its scope
and which reference applies to a timing-sensitive DOS platformer on my TV.
```

It should locate SKILL.md and choose relevant action/DOS guidance. This checks
discovery; it does not prove game compatibility or authorize TV installation.

## Updates

For a Git-based installation, review changes and update the chosen checkout:

```sh
git -C "$HOME/.agents/skills/port-samsung-tv-games" pull --ff-only
```

Replace the path for Claude Code, Cursor, or a project installation. Keep local
edits before updating; do not delete an installation to bypass a conflict. For
Claude account uploads, rebuild the ZIP and update the uploaded skill through
that interface. Installing this repository does not update any TV game.

## Other tools

An agent supporting the [Agent Skills format](https://agentskills.io/specification)
can load the same SKILL.md and references. Use that tool's documented installation
location and invocation syntax; do not assume a generic chat reads local folders.

Documentation paths and UI steps were checked against the linked official sources
on 2026-10-28. Discovery and hardware access depend on your installed client and
organization settings.
