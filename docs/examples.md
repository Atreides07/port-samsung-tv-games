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
| [Civilization gameplay](screenshots/civilization.png) | `output/playwright/civilization/original-map.png` | Browser verification, original Russian UI, 1920×1080 |
| [Civilization ship orders](screenshots/civilization-orders-en.png) | `output/playwright/skill-gallery-en/civilization.png` | Opera, English UI preview, 1920×1080 |
| [Dune II](screenshots/dune-ii.png) | `output/playwright/dune-controls/moving.png` | Browser verification, original Russian UI, 1920×1080 |
| [Prince of Persia](screenshots/prince-of-persia.png) | `output/playwright/skill-gallery-en/prince-of-persia.png` | Opera, English UI preview, 1920×1080 |
| [Zuma Deluxe](screenshots/zuma.png) | `output/playwright/skill-gallery-en/zuma.png` | Opera, English UI preview, 1920×1080 |

The X-COM, Prince of Persia, and Zuma screenshots were captured on 2026-10-28
from running local ports in isolated Opera browser contexts. Their remote-control
hints and Zuma interface text were translated in the live page before capture.
X-COM and Prince of Persia already render their native game text in English.

Dune II and Civilization gameplay screenshots show the actual game field without
a modal order menu. Both retain the original Russian HUD and remote-control hints
and are copied without alteration from the verification artifacts listed above.

The additional Civilization ship-order screenshot is an English documentation
preview captured from the running port in Opera on 2026-10-28. Its panel text and
hints were translated in the live page. CSS clipping omits the top 5% and left 25%
of the native canvas to avoid the untranslated HUD; the image is labeled
ENGLISH UI PREVIEW. The original DOS program and gameplay interface remain Russian.

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
