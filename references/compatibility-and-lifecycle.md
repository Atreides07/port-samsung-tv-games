# Compatibility, Startup, Lifecycle, and Updates

Read for a new port or changes to the runtime, loading, memory, storage, or app
lifecycle. Keep the target profile small and factual; do not require a broad device
matrix when the user requests one TV.

## Target Profile and Startup

Record the TV model/model year, installed Tizen/Web engine, remote type, runtime
version, internal framebuffer, and asset/audio formats. Samsung publishes a
[Web engine and feature matrix](https://developer.samsung.com/smarttv/develop/specifications/web-engine-specifications.html).
Use the target's actual requirements rather than universally downgrading every
port to ES5 or assuming modern desktop APIs are present.

Check JS parsing and required WASM, WebGL/Canvas, audio, worker, and local-loading
features that the chosen runtime actually uses. Provide an early error view that
can run on the target if the main runtime cannot load. Probe optional APIs before
use; unsupported syntax needs a compatible build, not a check after parsing.

Time cold startup to the first visible image and the first usable game action.
Measure peak memory during archive expansion and audio/image decoding. Avoid
holding compressed data, redundant extracted copies, and large decoded buffers
longer than necessary. A successful warm run does not establish cold-start safety.
A failed load should offer retry or a return path using the remote, without
repeatedly discarding saves or restarting into the same failure.

## Resource Measurement

Separate JS heap, WASM heap, graphics/audio buffers, and total process resources.
Check the applicable model's limits rather than treating one historical heap size
or a documentation example as a universal cap. Use supported device APIs or tools;
newer memory APIs must not become a startup dependency on older TVs.
Samsung notes that Web Inspector does not measure total system memory and cannot
capture app initialization in its normal attachment workflow:
[Hardware Resource Management](https://developer.samsung.com/smarttv/develop/ai-tv-platform-standards/hw-resource-management.html).

Repeat load/restart/menu cycles and run a representative long session when the
change can leak resources or accumulate state. Choose the duration for the game
and risk; do not impose one expensive soak on every small correction. Check for
retained DOM/listeners, audio voices, buffers, repeated decoding, and degraded
frame pacing. Measure with and without diagnostic instrumentation when its cost
could affect the result.

## Hide, Resume, and Termination

Use actual visibility notifications and clear pending input on hiding. Samsung
pauses JavaScript execution while the app is hidden; background timers are not a
reliable place for cleanup or continuing simulation. See
[Multitasking](https://developer.samsung.com/smarttv/develop/guides/fundamentals/multitasking.html).

Exercise Home → another app → return, source changes, relevant power/standby
behavior, and a fresh launch after process termination. Distinguish an in-memory
resume from recovery of a durable save. Persist valid checkpoints during normal
play or explicit saving; an exit handler may never run. For DOS, do not serialize
unfinished files just because visibility changed.

After resume, reset the elapsed-time baseline, clear stale input/queued commands,
restore focus, and honor mute/pause state. Do not let the player move, take damage,
or hear unexpected audio before the resumed screen and controls are ready.

## Save Compatibility and Installation Updates

Distinguish the original game's saves from emulator snapshots: snapshots may depend
on a particular runtime and memory layout. Document what a save restores, such as
an entire session, a level checkpoint, or only a high score. Do not promise full
session recovery when the original format does not provide it.

Version a changed data schema and test a real previous-format fixture. Validate
and migrate a copy, committing only after it loads successfully; a failed migration
must leave the previous valid data recoverable. Test old installation → save →
update in place → load. Export/backup is appropriate when supported and needed for
a risky migration, not a reason to add a network service to an offline game.

Preserve application/package IDs and the author certificate. Samsung requires the
same author certificate for updates of a published app:
[Quick-start Guide](https://developer.samsung.com/smarttv/develop/getting-started/quick-start-guide.html).
Use existing signing profiles without copying keys or credentials into source
control. Do not uninstall as a shortcut for fixing an update failure.

## Packaged Offline Acceptance

Use the project's existing package/install tools. If they enumerate games, update
the accepted name, app-directory/ID mapping, asset extensions, and related checks.
A new registry or framework is unnecessary when a small existing mapping suffices.

Check transitive local assets, including CSS URLs, JS-loaded audio/images, workers,
and WASM that exist in the selected runtime. Run the final signed WGT with external
network access unavailable, without changing the user's network/VPN settings.
Reach delayed content and at least one later scene. A passing HTTP preview or a
scan of index.html alone cannot establish packaged offline behavior.
