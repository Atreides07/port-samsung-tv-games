# Port Examples and Screenshot Provenance

These examples come from the author's Samsung TV game project. They illustrate
the kinds of problems that informed this skill. This repository publishes the
workflow and selected screenshots, not the game ports or their original content.

## Examples

| Game | Port approach | What the example demonstrates |
| --- | --- | --- |
| X-COM: UFO Defense | Original DOS program in a local js-dos runtime | Battlescape movement, context-sensitive actions, and separate geoscape/tactical save sets. |
| Sid Meier's Civilization | Original DOS program in a local js-dos runtime | Object-specific orders, persistent sentry duty, and a full catalog with verified/blocked/unknown availability. |
| Dune II | Original DOS program in a local js-dos runtime | Directional quick orders, local audio, and tuning against measured gameplay speed. |
| Prince of Persia | Original DOS program in a local js-dos runtime | A running-jump adapter for sequential remote input, hold ownership, and gameplay-result checks. |
| Zuma Deluxe | HTML/Canvas adaptation using original resources | Aim/fire controls, visible hints, and image validation with Canvas fallback for unusable WebGL output. |

The original DOS programs execute their own rules. Zuma is an adaptation and
does not execute the original Windows program. These distinctions matter when
assessing fidelity, completeness, and what an automated test can prove.

## Included captures

| Published image | Source capture in the original game project | Environment |
| --- | --- | --- |
| [X-COM](screenshots/xcom.png) | `output/playwright/skill-gallery-en/xcom.png` | Opera, English UI preview, 1920×1080 |
| [Civilization](screenshots/civilization.png) | `output/civilization-context/quick-ship.png` | Browser verification, original Russian UI, 1920×1080 |
| [Dune II](screenshots/dune-ii.png) | `output/playwright/dune-controls/orders.png` | Browser verification, original Russian UI, 1920×1080 |
| [Prince of Persia](screenshots/prince-of-persia.png) | `output/playwright/skill-gallery-en/prince-of-persia.png` | Opera, English UI preview, 1920×1080 |
| [Zuma Deluxe](screenshots/zuma.png) | `output/playwright/skill-gallery-en/zuma.png` | Opera, English UI preview, 1920×1080 |

The X-COM, Prince of Persia, and Zuma screenshots were captured on 2026-10-28
from running local ports in isolated Opera browser contexts. Their remote-control
hints and Zuma interface text were translated in the live page before capture.
X-COM and Prince of Persia already render their native game text in English.

Dune II and Civilization retain the original Russian screenshots, including the
native HUD and remote-control panels. These two PNGs are copied without alteration
from the original verification artifacts listed above. Their original DOS programs
and port interfaces remain in Russian.

The English previews are documentation presentation, not a claim that the installed
ports have received a complete localization. No game executables, game rules, or
original art were changed. The PNGs were captured directly from the original ports
or the live English previews; no image retouching or AI-generated game imagery was
used. Source game files, test fixtures, and capture runners belong to the original
project and are not distributed in this skill repository.

## What is and is not established

The images show the rendered scenes and TV-oriented interface. A still image
does not establish input latency, sustained frame rate, save integrity, audible
TV speakers, or comfort with a physical remote. Those require separate checks.
Historical tuning observations in [porting-notes.md](../references/porting-notes.md)
are tied to particular games, runtimes, and devices; do not treat them as current
benchmarks or universal emulator presets.

Game names and depicted artwork remain associated with their respective creators
and rights holders. The repository's MIT license covers its original instructions
and helper code, not the third-party game imagery in these screenshots.
