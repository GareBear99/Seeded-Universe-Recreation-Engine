# Architecture Overview

## High-level summary

This repo combines three layers:

1. **Universe simulation / observer layer** in browser HTML/JS prototypes
2. **Synth shell / signal layer** in a blueprint-gated browser runtime
3. **ARC-Core service layer** in a FastAPI package under `ARC_Console/`

## Front-end entry points

- `MasterControl.html` — split-screen host for the main combined experience
- `sure/universe_observer_v16_vision.html` — primary universe observer
- `universe_observer_prototype_v8_local_region_chemistry.html` — earlier chemistry-focused observer
- `synth/index.html` — Synth shell runtime
- `universe_bridge.js` — bridge logic between universe and Synth

## ARC-Core package

The `ARC_Console/arc/` package contains:

- `api/` — FastAPI app, startup, and routes
- `core/` — config, DB, auth, schemas, simulation, utilities, risk
- `geo/` — geometry and geospatial estimators
- `services/` — cases, proposals, watchlists, notebook, ingest, geospatial, universe, audit, graph, connectors, auth/bootstrap
- `ui/` — dashboard, graph, timeline, signals, geo, and cases pages

## Notable capabilities visible in code

- event ingest and entity retrieval
- graph snapshots and timelines
- watchlists and cases
- proposals and approvals
- evidence export
- notes / notebook features
- auth bootstrap and sessions
- connector create/list/poll flow
- geospatial structures, sensors, geofences, tracks, heatmaps, incidents, evidence packs
- universe record create/list routes

## Ecosystem position

This repo is the simulation/emergence node in a broader stack:

- [Proto-AGI](https://github.com/GareBear99/Proto-AGI)
- [ARC-Core](https://github.com/GareBear99/ARC-Core)
- [ARC-Turbo-OS](https://github.com/GareBear99/ARC-Turbo-OS)
- [Arc-RAR](https://github.com/GareBear99/Arc-RAR)
- [Proto-Synth_Grid_Engine](https://github.com/GareBear99/Proto-Synth_Grid_Engine)
- [Seeded-Universe-Recreation-Engine](https://github.com/GareBear99/Seeded-Universe-Recreation-Engine)
- [LuciferAI_Local](https://github.com/GareBear99/LuciferAI_Local)
- [AGI_Photon-Quantum-Computing](https://github.com/GareBear99/AGI_Photon-Quantum-Computing)

## Honest status

The repo already has meaningful implementation surface, especially on the ARC side, but it is still a prototype/concept package rather than a complete scientific or production-grade universe platform.
