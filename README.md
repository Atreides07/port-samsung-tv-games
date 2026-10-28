# Samsung TV Game Ports

[![Validate](https://github.com/Atreides07/port-samsung-tv-games/actions/workflows/validate.yml/badge.svg)](https://github.com/Atreides07/port-samsung-tv-games/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An Agent Skill for bringing offline games to Samsung Smart TV / Tizen with
controls people can actually use from the sofa.

It guides an AI coding agent through native HTML/Canvas adaptations and local
DOS runtimes: remote input, contextual commands, original audio, reliable saves,
performance measurement, and verification of the final TV package.

**[Install for Codex, Claude, or Cursor](docs/installation.md)** ·
**[Download skill ZIP](https://github.com/Atreides07/port-samsung-tv-games/releases/latest/download/port-samsung-tv-games.zip)** ·
**[Read the skill](SKILL.md)** · **[Port examples](docs/examples.md)**

## Games behind the workflow

These are actual captures from the author's ports. All five images below are
**browser verification screenshots**, not photographs or performance measurements
of a physical TV. The captured interfaces use Russian labels; the skill and
installation guide are in English.

| X-COM: UFO Defense | Dune II |
| --- | --- |
| ![X-COM Battlescape with remote-control hints](docs/screenshots/xcom.png) | ![Dune II contextual order panel operated by remote directions](docs/screenshots/dune-ii.png) |
| Original DOS game with tactical movement and contextual actions. | Original DOS game with a compact directional order panel. |
| **Prince of Persia** | **Zuma Deluxe** |
| ![Prince of Persia running-jump scenario with remote-control hints](docs/screenshots/prince-of-persia.png) | ![Zuma TV adaptation with aim, fire, ball swap, and precision controls](docs/screenshots/zuma.png) |
| Original DOS platformer with a running-jump input adapter. | HTML/Canvas adaptation using original resources; it does not execute the Windows game. |

**Sid Meier's Civilization — contextual ship orders**

![Civilization quick-order panel with sentry, skip-turn, wait, and all-command actions](docs/screenshots/civilization.png)

Original DOS strategy game with object-specific quick actions, persistent sentry
duty, and a complete command catalog with availability explanations.

See [examples and capture provenance](docs/examples.md) for the demonstrated
behaviors and the limits of what these screenshots prove. Game archives,
executables, runtime bundles, and installable TV games are not distributed here.

## What the skill covers

- **Controls first:** arrows, OK, and Return; held keys, focus, useful shortcuts,
  action timing, and contextual command availability.
- **Feasibility before integration:** target TV/runtime compatibility and an early
  test of the game's hardest relevant interaction.
- **Offline operation:** local assets, original audio where available, and final
  package checks with the network unavailable.
- **Durable progress:** complete save transactions, lifecycle recovery, previous
  version updates, and careful save migration.
- **Measured performance:** realistic internal resolution, Canvas/WebGL validation,
  startup and peak memory, frame pacing, and appropriately scoped long sessions.
- **Honest verification:** browser results, physical-TV traces, speaker listening,
  and manual-remote play are reported separately.

A complete-port request includes controls and performance work. A request for a
plan, audit, or narrow fix keeps that scope. The skill does not authorize changing
other games, network/VPN settings, or publishing third-party game assets.

## Install and use

The repository root is the skill directory. Choose **one** installation location
per agent; the full [installation guide](docs/installation.md) includes personal
and project paths, Windows commands, updates, and Claude ZIP upload.

| Tool | Personal installation | Invoke |
| --- | --- | --- |
| Codex | `~/.agents/skills/port-samsung-tv-games/` | `$port-samsung-tv-games` |
| Claude Code | `~/.claude/skills/port-samsung-tv-games/` | `/port-samsung-tv-games` |
| Cursor | `~/.cursor/skills/port-samsung-tv-games/` | Select `/port-samsung-tv-games` in Agent chat |
| Claude web/Desktop skills | Upload the packaged skill ZIP in Customize → Skills | Ask to use the Samsung TV game-porting skill |

Example request:

```text
Use $port-samsung-tv-games to port this game to my Samsung Tizen TV.
Keep the original rules and audio, make the core loop usable with arrows,
OK, and Return, and verify saves and performance. Report browser checks
separately from physical-TV checks.
```

For a focused correction:

```text
Use the Samsung TV Game Ports skill to fix running jumps on this remote.
Keep the existing game rules, application IDs, saves, audio, and rendering.
Verify the actual jump and affected input regressions.
```

An agent needs access to the game project and appropriate build/test tools.
Actual installation requires the user's authorized TV access and signing setup.
A cloud chat can review or prepare files, but it needs an explicitly connected
execution environment to inspect your local project or operate your TV.

## Structure

```text
SKILL.md                              Shared workflow and acceptance criteria
agents/openai.yaml                    Codex UI metadata; optional for other agents
references/action-controls.md         Timing-sensitive controls
references/contextual-commands.md     Strategy and object-specific orders
references/compatibility-and-lifecycle.md
references/porting-notes.md           Historical DOS and rendering case studies
docs/installation.md                 Agent-specific installation instructions
docs/examples.md                     Examples and screenshot provenance
scripts/validate.py                   Metadata, links, and package hygiene checks
scripts/package.py                    Minimal portable skill ZIP builder
```

## Validate and package

Python 3.10+ and PyYAML are needed only for the repository checks and packaging;
using the instruction files does not require a Python dependency.

```sh
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/package.py
```

The ZIP is written to `dist/port-samsung-tv-games.zip`. It contains one
`port-samsung-tv-games/` folder with the instructions, references, UI metadata,
and license; it excludes screenshots, development files, and game content.
GitHub Actions runs the same checks and publishes the ZIP as a workflow artifact.

## Contributing

Keep the core skill focused and move substantial conditional guidance into a
reference linked from SKILL.md. Explain the real porting failure or scenario
behind a change, add a meaningful check for changed helper logic, and run the
validation commands above. Do not commit game archives, signing keys, credentials,
private device details, or claims of hardware testing without evidence.

Historical case studies are observations from particular ports, not universal
DOS presets or promises that every Samsung model will behave the same way.

## License and game credits

Original skill instructions and helper code are [MIT licensed](LICENSE).
The screenshots illustrate third-party games and are excluded from that license;
no rights to their artwork, trademarks, or game assets are granted.

Examples credit the original games and creators/publishers: X-COM: UFO Defense
(MicroProse), Sid Meier's Civilization (MicroProse), Dune II (Westwood Studios),
Prince of Persia (Jordan Mechner /
Brøderbund), and Zuma Deluxe (PopCap Games). Their names identify the examples;
this project is independent of Samsung and those game creators.
