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

| Published image | Capture artifact in the original game project | Environment |
| --- | --- | --- |
| [X-COM](screenshots/xcom.png) | `output/skill-publication/tv-captures/xcom.png` | Physical Samsung TV, tactical battle, 1920×1080 |
| [Civilization gameplay](screenshots/civilization.png) | `output/skill-publication/tv-captures/civilization.png` | Physical Samsung TV, original Russian game, 1920×1080 |
| [Civilization ship orders](screenshots/civilization-orders.png) | `output/skill-publication/tv-captures/civilization-orders-en-tv-2026-10-29.png` | Physical Samsung TV, English panel preview, 1920×1080 |
| [Dune II](screenshots/dune-ii-gameplay-tv.png) | `output/skill-publication/tv-captures/dune-ii-gameplay-2026-10-29.png` | Physical Samsung TV, mission gameplay, 1920×1080 |
| [Prince of Persia](screenshots/prince-of-persia.png) | `output/skill-publication/tv-captures/prince-of-persia.png` | Physical Samsung TV, original DOS gameplay, 1920×1080 |
| [Zuma Deluxe](screenshots/zuma.png) | `output/skill-publication/tv-captures/zuma.png` | Physical Samsung TV, HTML/Canvas adaptation, 1920×1080 |

Four images were captured on 2026-10-28. Dune II was recaptured on 2026-10-29
after selecting a unit and issuing a movement order, with no order menu open.
The English Civilization ship-order panel was captured on 2026-10-29.
All captures come from a Samsung UE65TU8570UXRU running Tizen 5.5 and Chromium 69.
The capture session verifies the device's
SMART-TV user agent, application ID, 1920×1080 application viewport, and game
state. The Civilization ship-order panel was translated in the live TV page for
this capture; its native DOS canvas and all text outside the panel were verified
unchanged. Other images retain their original text. No cropping, retouching,
or generated game imagery is used.

This TV does not return frames through CDP `Page.captureScreenshot` or screencast.
Instead, its Web Inspector exports the application's painted render layers using
`LayerTree.makeSnapshot` and `LayerTree.replaySnapshot`. An offscreen Canvas on the
**same TV** composites those layer bitmaps in their existing order, positions,
and transforms, then exports the PNG. This captures both the game and its remote
interface without rendering the game in a desktop browser. It is an application
render capture, not a camera photograph, HDMI capture, or measurement of the TV's
physical panel processing.

Temporary signed copies use separate application identities and storage origins.
X-COM and Dune II load test checkpoints; Civilization uses a prepared ship
checkpoint. Prince of Persia and Zuma run their normal gameplay. Capture copies
preserve the source game rules, rendering, audio, and interface; test-only startup
seeding and Civilization inspection hooks prepare the scenes. The original game
applications and user saves remain separate. The temporary applications and SDB
forwarding are removed after capture. Per-frame JSON records, raw layer PNGs,
source hashes, and install logs remain in the original project's capture folder;
game content and the capture utilities are not distributed with this skill.

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
