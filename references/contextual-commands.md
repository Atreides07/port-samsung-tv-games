# Contextual Commands


For games with a set of orders/actions, especially those with different units or
objects:

- Show frequent actions appropriate to the current object in the quick panel.
  Account for type, remaining actions, cargo/resources, tile/target, and required
  discoveries when they actually constrain the order. Keep directional assignments
  consistent for related functions; do not fill slots with clearly unsuitable orders.
- If the original supports persistent waiting, sentry duty, or holding position,
  provide a short path to that mode: repeating "skip turn" every turn is awkward.
  Distinguish skipping, passing priority to the next unit, and persistent waiting;
  explain how to wake the unit.
- Provide a visible short path from the quick panel to all commands. ↑ suits such
  a panel if it does not conflict with the game's controls. Do not reassign ↑
  movement on the main screen for the catalog or impose that button on other genres.
- Keep a full list with clear statuses: ✓ available in the verified context;
  — a known restriction and its reason; ? some conditions are checked by the original.
  Do not present uncertainty as availability. Hide unsuitable quick-command buttons
  or replace them with useful ones; keep explanations accessible with the remote in
  the catalog. A focusable aria-disabled item or another accessible mechanism must
  let users read the reason, while confirming a prohibited item must not send input
  to the game.
- Share the availability check between listing and execution. After waiting in a
  queue, an animation, or a window change, recheck the conditions and object identity
  so the order does not reach a different unit. Selecting/waking an object must not
  itself require an active unit.
- Take a lightweight context snapshot when opening the panel or on a meaningful
  change; do not scan all memory/DOM every frame for hints. In DOS, show conditions
  based on verified data while leaving the original as the final authority on rules.

For validation of the original game's data and a worked example, see
[porting-notes.md](porting-notes.md). A game with a few
simple actions may not need a separate multilevel catalog.


## Verification

Test different object types, an allowed/prohibited pair, an unknown condition,
and an active-object change while an order is queued. Confirm the result in the
original game state, not just a key code or press counter. Persistent waiting
needs a next-turn test, a documented wake-up path, and save/load verification
when that mode should survive them. Measure panel construction on the target TV;
a synchronous JS/DOM call does not measure total remote-to-visible latency.
