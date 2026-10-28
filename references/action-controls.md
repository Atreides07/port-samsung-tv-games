# Action and Timing-Sensitive Controls

Use this guidance for platformers, shooters, racing games, and other games where
movement and action timing matter. A strategy-style command catalog is not a
substitute for a playable primary loop.

## Test the Hard Action Early

Choose a real obstacle from the original: a running jump, movement while firing,
a ledge grab, a quick reversal, or a precise stop. Check what the actual remote
emits for overlapping buttons, release order, repetition, and short taps. Browser
keyboard chords and synthetic TV events do not establish physical-remote support.
Do not assume all IR and Bluetooth remotes behave alike.

Create a short sequence that works with arrows, OK, and Return. Prefer the original
mechanics with a deliberate input adapter over changes to physics or difficulty.
If the necessary combination is impractical, consider a small input buffer, a
visible mode toggle, or a clearly labeled assisted command. Explain any change in
behavior and obtain the user's choice when the tradeoff changes the requested game.

## Keep Input Ownership Explicit

- Track physical holds separately from synthetic presses. Releasing a synthetic
  jump must not release a physical direction the player is still holding.
- Cancel buffered actions and direction memory on pause, blur, hiding, or a changed
  gameplay context. An old command must not fire after returning from a menu.
- Derive buffer windows and press duration from the original game's acceptance
  timing and hardware observations; a fixed timer copied from another game is not
  a calibration. Prefer observable readiness over blind multi-action macros.
- Long OK delays the short action when the distinction is made on keyup. Measure
  the resulting response before assigning jump, fire, or another frequent action
  to that mechanism. Retain a quick visible route to a rare alternate mode.
- Avoid an extra game loop just to maintain input state. Use the existing input
  events/tick and a bounded timer only when the observed behavior requires it.

## Acceptance

Test both directions, a short tap, overlapping holds, missing/repeated keydown
flags, releasing in either order, cancellation, and the ordinary action after
leaving the assisted mode. Confirm the actual trajectory, hit, landing, or other
original-game result; sending the intended key codes is insufficient.

One Prince of Persia port used a short remembered movement direction to make a
running jump possible with sequential arrows. It was checked in an open corridor;
a low-ceiling room alone would not have established the intended trajectory.
That example motivates the test, not universal timing constants.
