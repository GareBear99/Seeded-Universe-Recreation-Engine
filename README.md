# Seeded Universe Recreation Engine

A deterministic, seed-first universe simulation project that connects a browser-based universe observer, a Synth control shell, and ARC-Core into one broader AGI / simulation stack.

This repository is the public-facing concept and prototype package for a larger long-range goal: reconstructing a universe from seed-governed math first, rendering second, then using observation, control, and receipted intervention layers to study emergence, chemistry, life potential, and intelligence signatures.

## What this repo currently contains

This package is not a single monolith. It includes three connected layers:

- **Universe Observer / SURE prototype**: browser-based seeded universe and planet simulation views
- **Synth control shell**: a deterministic, blueprint-driven signal/control surface
- **ARC-Core console**: a FastAPI-based intelligence and receipt layer for records, cases, graph state, watchlists, proposals, notes, and universe records

Top-level entry points:

- `MasterControl.html` — split-screen launcher for universe + synth + bridge flow
- `sure/universe_observer_v16_vision.html` — main universe observer view
- `universe_observer_prototype_v8_local_region_chemistry.html` — earlier chemistry-focused prototype
- `synth/index.html` — Synth shell and module runtime
- `ARC_Console/` — ARC-Core API and UI package
- `launch.py` — local launcher for ARC + browser front-end

## Why this exists

The broader thesis behind this repo is:

- reality can be modeled as a seed-rooted, causal, math-governed system
- visual output should derive from authoritative simulated state rather than decorative shortcuts
- chemistry, habitability, life potential, and intelligence signatures should emerge from deterministic rules rather than hardcoded outcomes
- any observation, intervention, or control attempt should be receipted and comparable against the canonical seed path

This repo is one part of a larger ecosystem pursuing that architecture.

## Related repositories in the stack

- [Proto-AGI](https://github.com/GareBear99/Proto-AGI)
- [ARC-Core](https://github.com/GareBear99/ARC-Core)
- [ARC-Turbo-OS](https://github.com/GareBear99/ARC-Turbo-OS)
- [Arc-RAR](https://github.com/GareBear99/Arc-RAR)
- [Proto-Synth_Grid_Engine](https://github.com/GareBear99/Proto-Synth_Grid_Engine)
- [Seeded-Universe-Recreation-Engine](https://github.com/GareBear99/Seeded-Universe-Recreation-Engine)
- [LuciferAI_Local](https://github.com/GareBear99/LuciferAI_Local)
- [AGI_Photon-Quantum-Computing](https://github.com/GareBear99/AGI_Photon-Quantum-Computing)

## Where this repo fits in that stack

This project is the **simulation / emergence / observation layer**.

- **Proto-AGI** frames the broader intelligence direction.
- **ARC-Core** provides records, graphing, cases, proposals, watchlists, receipts, and operator-facing APIs.
- **ARC-Turbo-OS** points toward a seed-rooted, event-spine runtime where state can be reconstructed and reused.
- **Arc-RAR** explores portable archive / package handling across systems.
- **Proto-Synth_Grid_Engine** provides the Synth shell and execution surface logic.
- **LuciferAI_Local** is the local model/runtime side for intelligence augmentation.
- **AGI_Photon-Quantum-Computing** represents the future compute/control substrate for higher-speed cognition and hardware orchestration.
- **Seeded-Universe-Recreation-Engine** is where seeded world generation, chemistry, life potential, signal observation, and comparative intervention concepts meet.

## Current architecture

```text
MasterControl.html
├── sure/universe_observer_v16_vision.html
│   ├── seeded universe / planetary / chemistry / habitability logic
│   ├── life-potential and civilisation-signature modeling
│   └── bridge messages to Synth
├── synth/index.html
│   ├── blueprint-gated shell runtime
│   ├── scanner / ship / HUD modules
│   ├── validator / recovery / authority helpers
│   └── signal and receipt interactions
├── universe_bridge.js
│   ├── universe → synth contact extraction
│   ├── synth → universe receipt flow
│   └── bridge event logging
└── ARC_Console/
    ├── FastAPI app and routes
    ├── auth / cases / watchlists / proposals / notes / connectors
    ├── geospatial and graph services
    └── universe record ledger endpoints
```

## Code surface audit

This repo was read before documentation updates.

Audit snapshot of the package in this repo:

- **55 files** total
- **31 Python files**
- **149 Python functions**
- **20 Python classes**
- **0 Python syntax errors** in the audited package

The ARC layer is materially broader than a minimal demo. It already includes:

- FastAPI app boot and route registration
- auth/session bootstrap and role resolution
- event ingest and entity listing
- graph snapshot and timeline views
- watchlists, cases, evidence, proposals, and approvals
- notes, connectors, and polling hooks
- geospatial structures, geofences, heatmaps, track estimation/import, and evidence export
- universe record creation/listing

See [`docs/CODE_SURFACE_AUDIT.md`](docs/CODE_SURFACE_AUDIT.md) and [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Quick start

### Browser-only front end

Open:

- `MasterControl.html` for the split-screen launcher
- `sure/universe_observer_v16_vision.html` for the universe observer only
- `synth/index.html` for the Synth shell only

### ARC + front end launcher

```bash
python3 launch.py
```

Useful options:

```bash
python3 launch.py --check
python3 launch.py --arc-only
python3 launch.py --sure-only
python3 launch.py --master-only
```

### ARC dependencies

```bash
pip install -r requirements.txt
```

Then run:

```bash
python3 launch.py --arc-only
```

## What is real today vs. what is aspirational

What is already present in this repo:

- browser prototypes for seeded universe observation
- browser Synth control/runtime surfaces
- JavaScript bridge logic between simulation and Synth layers
- a real ARC-Core FastAPI service surface inside `ARC_Console/`
- launch tooling for local startup

What remains aspirational / long-range:

- complete physically rigorous universe reconstruction
- full-life emergence validation from first principles
- production-hardened cross-machine orchestration
- large-scale long-run evidence proving intelligence emergence
- deeper integration with the broader ARC / Lucifer / Synth stack

## SEO / discoverability framing

This repository is best understood as a public concept/prototype package for:

- seeded universe simulation
- deterministic world generation
- emergent life and civilisation modeling
- browser-based AGI simulation interfaces
- ARC-linked simulation records and receipts
- Synth-mediated control and observation
- SSOT / seed-rooted runtime architecture

See [`docs/SEO_PROMOTION.md`](docs/SEO_PROMOTION.md) for suggested repo description, topic tags, promotion copy, and public-facing phrasing.

## Recommended GitHub About description

`Seeded universe simulation, Synth observer shell, and ARC-linked intelligence records for a deterministic AGI / emergence stack.`

## Suggested repository topics

`seeded-universe, universe-simulation, deterministic-systems, world-generation, emergent-life, agi, cognitive-architecture, fastapi, simulation, systems-architecture, chemistry-simulation, habitability`

## Repo hygiene files added in this package pass

- `requirements.txt`
- `docs/ARCHITECTURE.md`
- `docs/STACK.md`
- `docs/CODE_SURFACE_AUDIT.md`
- `docs/SEO_PROMOTION.md`
- `docs/REPO_SETUP_CHECKLIST.md`
- `.github/workflows/ci.yml`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/pull_request_template.md`
- `.gitignore`
- `LICENSE`
- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CODE_OF_CONDUCT.md`
- `Makefile`

## Author

Gary Doman

Canonical ecosystem provenance: DOMAN_ORIGIN_RECORD
