# Verified Cases and Usage Guidance

These cases come from the Samsung project on UE65TU8570UXRU / Tizen 5.5 /
Chromium 69 in October 2026. Check the current source, device, and reports.
The values below are starting points for experiments, not performance guarantees
for a new game.

## DOS: Choose Based on Measurements

- Reuse a compatible local runtime and its licenses/corresponding source code;
  respect the capabilities of the target JS/WebAssembly version.
- In Dune II, machine=vgaonly enabled a doubled 640×400 scanout. A compatible
  svga_s3 mode produced a true 320×200 image and reduced pixel transfers fourfold.
  Begin testing a VGA game with a compatible mode, but retain EGA/Tandy and other
  modes when the original requires them. Measure the actual canvas.width/height.
- Preserve the original graphics: scaler=none and CSS aspect correction are often
  more useful than expensive scaling inside the emulator. Check the palette,
  text, and mouse calibration.
- In js-dos 6.22.60, sync_sleep already yields to the browser through postMessage.
  An extra 8 ms wait slowed Dune. Do not add it automatically; if another original
  game needs adjustment, justify it with a hardware comparison.
- Dune used normal / max 80% limit 12000 / frameskip=1;
  fixed 12000 performed worse. On the TV, the first mission went from
  9.61 → 21.79 outputs/s, and the time to produce one slab went from
  10.72 → 7.79 s.
- Civilization used normal / max 50% limit 6000 / frameskip=1.
  In the same cursor scenario, the rate remained 25.91 outputs/s, while the p95
  interval of a 50 ms timer became 68.5 instead of 75.6 ms. The first 5 s of the
  intro slowed down: 13.55 → 11.34 outputs/s. Fixed 3000 slowed the intro further;
  fixed 6000 gave a p95 of 80.3 ms. Do not confuse these numbers with button-response
  latency.
- Compare normal/simple, fixed/adaptive budgets, and frameskip only when actually
  needed. A cycles setting labeled "50%" does not cap the browser process's total
  CPU usage: active emulation may occupy an entire core.
- These ports used 8 MiB of DOS RAM and a 64 MiB WASM heap; do not confuse the
  metrics or increase memory beyond the original game's needs.
- A rate of 22050 Hz, block 1024, prebuffer 40, and mixer master 65 worked here
  with volume headroom; these do not determine a universal sound-card type.
  Select the device the original needs: PC Speaker, AdLib/SB, or another driver.
  Do not disable required audio for FPS.
- In Dune, the archive's default configuration selected an unavailable MT-32 and
  disabled speech; check the original game's menus/SETUP first. Do not start by
  modifying the EXE.
- In browser testing of the supplied Russian Civilization, SB Pro 2 / OPL2 in this
  runtime produced a spurious tone and gaps in the music. SB Pro 1 / dual OPL2
  corrected the original ASOUND.CVL routing through ports 220/222. This is a setting
  for that specific bundle, not a preset for other DOS games. Check the driver/mixer,
  an individual effect, a music scene, and the absence of a stuck tone after an action.
  The earlier squeak on the TV did not recur; the restored music was checked in the
  PCM stream, but no one listened to it through the speakers.
- In Civilization, stdin redirection with "CIV.EXE < TV.IN" selected hardware but
  interfered with later dialogs. Use verified normal key presses.
- Recalculate absolute mouse coordinates using the actual Canvas rect and native
  framebuffer. Do not calibrate them once to the browser window size.
- Pixel masks/hashes are acceptable for a specific unchanged screen; record the
  asset version and tested region, and stop reading after recognition. Do not reuse
  another game's hashes or build continuous full-screen OCR.

## DOS: Verify Conditions Against the Original

- A key binding and menu label do not prove that the selected unit can execute an
  order. Check the original game's actual restrictions and result: type, action
  points, tile, passengers, discoveries, or window state.
- Reconstructed C, a comment, or one interpretation of memory can be wrong. When
  reading an ABI, verify its signature/bounds, record size, array stride, fields,
  signedness, and units against at least one independent source: machine
  instructions, a complete save block, the original menu, or an observed action.
  If the ABI is unconfirmed, do not guess addresses or send input that could reach
  the wrong object.
- In Civilization, the work table contains 12 entries of 6 words (12 bytes) each.
  A four-word declaration in reconstructed GAME.C proved incorrect; the 12-byte
  stride was confirmed by instructions in the original EXE. Incorrect 8-byte reads
  produced plausible but wrong permissions for mining and irrigation. Mining is
  prohibited in forests, while I starts terrain transformation; these distinct
  actions were verified in the original. Do not transfer this case's numbers or
  addresses to another game.
- Do not derive test expectations from the same assumption as the adapter. Use an
  independent example of original data and opposing conditions (such as
  forest/grassland/water, unlocked/locked technology, empty/loaded transport).
  Checking that R/I/M was sent without checking the original game's state change
  would have missed the error.
- For memory snapshots, keep reading separate from execution. Do not modify the
  EXE or rules to match the wrapper. A deferred order needs fresh context; if that
  context cannot be determined, provide an explanation/manual path.

## Canvas/WebGL: Verify the Image

In Zuma, scaled CPU Canvas overloaded page compositing. A separate Canvas layer
and HUD caching helped. WebGL then showed a high command count and NO_ERROR while
the board was black on the actual TV. The earlier claim of about 51 FPS proved
unsubstantiated. Pixel checks and a 2D fallback restored the image; the specific
2D scenario with 53 balls measured 24.89 frames/s.

Check WebGL contents at an appropriate time after drawing, while the buffer is
valid; use a scene known to contain a nonempty image so a valid black transition
is not mistaken for failure. Repeat the check on asset or context changes when
justified, rather than every frame. Test unavailable WebGL, a silently empty GPU
frame, and context lost; the game session and input must survive fallback.

## Verified Civilization 1.5.0 Example

This scheme was tested in this port, including game state on the physical TV via
key events. This scenario did not verify manual ergonomics on the real remote or
a long play session. Adapt the scheme for other genres and the user's choices.

- On the map, two matching arrows make a direct step, perpendicular arrows make
  a diagonal, and opposite arrows cancel. The first arrow shows the direction and
  waits for the second. A normal OK confirms/passes the turn, or clears a selected
  direction. This is the agreed scheme for this strategy game, not a requirement
  for every game.
- Return opens quick orders; ↑ inside the panel opens the full catalog.
  ↑ on the map retains movement. Return, OK opens pause and save.
- For ships/aircraft/settlers, ← means "Sentry / sleep" (S); for land troops, it
  means "Fortify" (F). Persistent waiting for a ship takes two presses instead of
  repeatedly skipping turns. The hint includes a manual wake-up path.
- → skips the rest of the turn, or sends the unit to the selected tile in cursor
  mode. ↓ offers construction for settlers, disembarking for loaded transports,
  and otherwise passing priority to the next unit. Without an active unit,
  selection/waking remains available.
- The catalog retains all orders with ✓/—/? and an explanation on focus. An
  unavailable item can be examined with the remote but cannot be sent to DOS.
  An unknown window subtype or spaceship readiness is not marked with an
  unconditional ✓.
- Tests verified the original Sentry state after two presses, the next unit
  remaining unaffected by a held key, actual road construction and forest clearing,
  mining prohibited in a forest without DOS input, different unit types, and
  transports with passengers.
- In a recognized dialog, OK confirms and Return cancels. In a city, short paths
  lead to production, workers, and the garrison. Leaving worker mode must not send
  Esc, which would also close the city itself.
- Saving continues until the CIVILn.SVE/MAP pair is closed and the final confirmation
  is completed; the user's slot is not assigned automatically.
- Panel construction on this TV took about 9.5 ms p95 over 30 synchronous JS/DOM
  calls. This is neither total remote-input latency nor a budget for every other game.

## Historical Evidence in the Original Samsung Project

These reports belong to the original private game project and are not bundled
with this skill repository. They are historical pointers, not reproducible
benchmarks supplied by this publication. In that project, look for
docs/tech.md, docs/STATE.md,
docs/milestones/13-dune-performance.md, docs/milestones/14-civilization-tv.md,
output/dune-performance/tv-comparison.json,
output/civilization-performance/tv-comparison.json, and output/zuma-black-screen/.
For the current command and audio example, see
docs/milestones/23-civilization-context-orders.md,
docs/milestones/22-civilization-audio.md, output/civilization-context/verification.json,
and output/civilization-audio/verification.json.
These point to the original evidence; their absence in another project does not
block work or turn old values into current measurements.
