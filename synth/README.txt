Synth — Dynamic Modules Shell (v2)

What this is
- A blueprint-gated shell builder (your "empty repo vessel") that becomes functional by attaching MODULE BLUEPRINTS.
- 3 blueprint lanes:
  1) Shell Blueprint (geometry + pivots/edges)
  2) Ship Module Blueprint (Master Control "eye" module)
  3) Scanner Module Blueprint (Synthesis Scanner probe + HUD window)
  (+ optional HUD module blueprint)

Run
- Open index.html (file:// is fine)
- Upload Shell Blueprint JSON first (use blueprint_octagon.json to test)
- Optionally upload module_ship_default.json / module_scanner_default.json / module_hud_default.json

Controls
- WASD: move the Master Control eye (inspection / camera intent)
- Mouse: aim vector
- C: toggle center reticle
- `: toggle debug overlay
- R: reset

Module blueprint format
{
  "moduleType": "ship" | "scanner" | "hud",
  "id": "NAME",
  "style": "iteration4" | "default",
  "config": { ... },
  "script": "optional JS hooks (advanced)"
}

Notes
- Core stays deterministic + lightweight (Canvas2D, fixed timestep, no per-frame allocations).
- All build actions remain ping-gated (GRANT/DENY receipts) and fail-closed SAFE_MODE on errors.


2026-03-06 Update: Eye-Lock synth visual pass added. The master ship is now drawn as a reticle-locked synth eye/pupil at screen center, with a dark glass lens shell, magenta plasma field, expanded crosshair geometry, and scanner bloom tuned toward the supplied reference image.
2026-03-06 Update: Eye-Core pass added. The center now uses a true pupil-disc stack with slit beam, heading-reactive ship glyph, breathing plasma ellipses, stronger reticle arcs, and subtle shell/grid distortion so movement reads as the universe moving around a fixed synth eye.


[v5 Eye-Scan update]
- Added scanner sweep wedge and ping-ring runtime behavior.
- Added deterministic contact markers derived from shell seed and route shape.
- Added presentation mode toggle (P) for clean cinematic view.
- Eye core now reacts to scan ping cadence and module identity.
- Preserved center-lock / eye-pupil architecture while pushing runtime behavior toward a real synth instrument surface.


Truth-Surface v6 update:
- blueprint-derived semantic contacts (pivot, wall, door, room, anomaly)
- deterministic shell warp keyed to shell seed
- scanner contact persistence and class-aware rendering
- ship/scanner module configs now visibly alter iris/slit and sweep behavior
- expanded debug truth surface for class counts and center-lock state


Anchor-Center v7 update:
- blueprint pivots are re-centered around their canonical centroid before shell construction
- the blueprint mass now sits on the reticle-aligned anchor instead of drifting off-center
- seed compilation now includes anchor-centered normalized blueprint geometry
- HUD/debug now report anchor mode, anchor source, centroid shift, and canonical blueprint hash
- this is the first pass toward exact two-way retraceable reticle/location seeding


Pole-Compass v8 update:
- added bottom-right pole detector / compass overlay locked to world pole directions
- compass labels N/E/S/W now derive from the camera-rotated global axes instead of screen-only decoration
- pole detector reports nearest locked pole, angular offset, and alignment state
- truth/debug panels now include pole lock telemetry

Authority-gated Phase B additions:
- Optional blueprint rooms[] and doors[] are now supported and compiled into occupancy truth.
- Save Bookmark (B) stores the live reversible coordinate seed + ARC address.
- Next Bookmark (N) recalls saved locations through the same seed authority path.
- Validator now reports authority state and bookmark count.


Matrix Synth v33 update:
- Route tiles are now persistent compute nodes instead of pure shell visuals.
- Compile synth roles at the reticle with 1-5 + G.
- Pulse the active node with X.
- Auto-seed a starter synth network from the blueprint with K.
- This is the first true computational shell pass: signals now move across the authoritative route graph.


[v35 additions]
J = semantic blueprint compile at reticle
Y = toggle autonomous synth executor
U = save persistent world state (also downloads JSON)
I = load persistent world state from localStorage


[v37]
- corruption ecology, builder embodiment, containment pulse, audit export


[v50 object-registry proof pass]
- Added authoritative object registry derived from shell occupancy + live tile evidence.
- Reticle packets now carry canonical proof stage (UNKNOWN / SUSPECTED / PROVEN) and visible state (HIDDEN / GHOST / SOLID).
- Survey save/load/export now include object-registry snapshots and stats.
- Authority validator now checks proof-stage / visible-state mismatches.
- Synth persistence keys/version bumped to v50_object_registry_proof_autosave.


[v51 builder commit completion pass]
- Added the missing builder-side completion loop after route mapping.
- Lifecycle now runs PLANNED -> INTEGRITY -> MAPPING -> VERIFIED -> COMMITTING -> COMPLETE -> EMPTY_REPO_READY.
- Authority objects now move through real commit state instead of stopping at mapped-only shell evidence.
- Commit progress is visible in the HUD/planner and is preserved in survey save/load.
- Persistence keys/version bumped to v51_builder_commit_autosave.


[v52 micro writeback + tile blueprint export pass]
- Added per-tile microcontroller writeback so tile micro summaries can feed authoritative shell occupancy and registry state.
- Added micro-derived authority fields (microAuthority / microBuildClass / microPenalty / microPopulation) into reticle packets and registry merges.
- Added survey save/load/export support for micro residency and aggregate writeback state.
- Added active-tile blueprint export (O) for the focused tile/subgrid.
- Persistence/version strings bumped to v52_micro_writeback_autosave.


[v53 completion pass]
- Import Tile Blueprint button added for round-trip tile blueprint workflow.
- Right dock now includes writeback status and command history panels.
- Focused tile blueprint exports can now be re-applied to the active tile/subgrid.


V54 completion pass
- strict tile blueprint schema lock on import
- rotating recovery autosave slots (3) with fallback restore
- helper split started via arc_schema_v54.js + arc_recovery_v54.js
- recovery hotkeys: [ previous slot, ] next slot, \\ restore selected slot


Production completion notes (v55)
- Authority writeback is now conflict-gated instead of always flowing directly into shell occupancy.
- Runtime audit helpers now surface commit drift, stale builder state, and repeated import failures.
- Right dock now includes a Builder Swarm status panel for recent commit receipts.
- Persistence/runtime version: v55_production_hardening.


V56 intent contract enforcement:
- All actions now pass through autowrap -> intent -> contract validation.
- Unknown intent no longer survives as a silent steady-state bucket; it is catalogued as a violation.
- Denied contracts now increment validator violations with source and event metadata.


[v58]
Boot stabilization pass: default module attach and blueprint tail work are now hardened so nonfatal post-load warnings do not collapse bootstrap into SAFE_MODE.


v59 notes:
- boot self-heal now repairs stale module/blueprint/shell flags before boot gating
- bootstrap clears stale boot_exception once shell + blueprint + all modules are valid


[v60]
Boot helper recovery: global sh/logPush stubs now exist so stale helper calls cannot keep the runtime in SAFE_MODE during fallback bootstrap.
