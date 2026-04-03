# Master Control — Complete System
**Universe Engine v16 + Synth Origin (Iteration 10) + ARC-Core**

---

## Start Here

### Full split-screen experience
```
MasterControl.html   ← open in browser
```
Both systems load side by side. The bridge connects them automatically.

### Individual components
```
sure/universe_observer_v16_vision.html   ← Universe Engine alone
synth/index.html                         ← Synth Origin alone
```

### ARC backend (optional)
```bash
pip install fastapi uvicorn pydantic
python launch.py
```

---

## What is this

Three systems, one doctrine.

### Universe Engine v16
A deterministic, seed-based universe simulation. From one seed, an entire
universe unfolds: stars, planets, atmospheres, oceans, geology, chemistry,
life, evolution, civilisations. Every state is already computed — we reveal
it, we don't create it.

Physics that work: Stefan-Boltzmann temperature, Jeans escape atmospheres,
water phase diagram life-capable check, Kepler orbits, tidal locking,
radioactive heating, supernova enrichment, Kardashev civilisations,
64-bit genome encoding, autocatalytic first replication events.

### Synth Origin (Proto-Synth Grid Engine Iteration 10)
The synth sits at the center of the universe. It is the signal instrument —
a blueprint-driven execution shell with a master control eye, scanner sweep,
route/signal network, and ARC-gated authority receipts.

In universe mode: the synth's scanner detects civilisations as contacts.
Its signal network becomes the communication backbone. Its eye watches
everything from the origin point.

### Universe Bridge v1
The bridge connects both systems without breaking causality. Universe state
flows to the synth as scanner contacts. Synth signal events flow back to
the universe as receipts. Every crossing is logged. TT-101 rules enforced.

---

## MasterControl.html Controls

| Control | Action |
|---|---|
| Split View | Side-by-side universe + synth |
| Universe Only | Full-screen universe engine |
| Synth Only | Full-screen synth origin |
| ⊙ Synth Center | Switch universe to L7 zoom — synth eye view |
| Test Bridge | Fire a bridge pulse, verify both systems respond |
| ARC Console | Open ARC truth ledger dashboard |
| Drag splitter | Resize the two panels |

---

## Zoom Levels (Universe Engine)

| Level | View |
|---|---|
| L0 | Cosmos — full universe |
| L1 | Galaxy cluster |
| L2 | Stellar system |
| L3 | Planet surface |
| L4 | Region cross-section |
| L5 | Molecule field |
| L6 | Atom patch |
| **L7** | **Synth Center — universe origin eye** |

Scroll wheel on canvas zooms through all levels.

---

## TT-101 Doctrine

Six rules that cannot be violated:

1. **Seed canonical** — seed is never changed to force outcomes
2. **Causality absolute** — no signal travels faster than c_sim
3. **Energy conserved** — ΔE_total = 0 always
4. **Intelligence emergent** — life cannot be hardcoded, only arise from physics
5. **Interventions receipted** — every perturbation logged in ARC
6. **Branch comparable** — modified universe never replaces canonical

---

## Synth Files

| File | Purpose |
|---|---|
| `synth/index.html` | Synth engine (v67) — the universe's signal instrument |
| `synth/blueprint_octagon.json` | Default shell geometry |
| `synth/module_ship_default.json` | Master Control eye module |
| `synth/module_scanner_default.json` | Synthesis scanner module |
| `synth/module_probe_default.json` | Probe planner module |
| `synth/module_hud_universe.json` | Universe HUD module (new) |
| `synth/arc_authority_v55.js` | ARC writeback authority |
| `synth/arc_schema_v54.js` | Tile blueprint schema |
| `synth/arc_recovery_v54.js` | Recovery slot system |
| `synth/arc_validator_v55.js` | Runtime validator |

---

## Architecture

```
MasterControl.html (split-screen launcher + bridge relay)
│
├── Universe Engine v16 (sure/universe_observer_v16_vision.html)
│   ├── Seed → physics → stars → planets → life → civilisation
│   ├── TT-101 doctrine enforcement
│   ├── Intelligence signature detector
│   ├── Intervention engine (epsilon → divergence → leverage)
│   ├── Signal propagation (c_sim limited)
│   ├── L0-L7 zoom stack
│   └── pushToSynthBridge() → universe state every frame
│
├── Universe Bridge (universe_bridge.js)
│   ├── onUniverseState() → extracts civ contacts → feeds synth
│   ├── onSynthOutput() → signal events → universe receipt
│   ├── generateUniverseBlueprint() → seed-matched synth geometry
│   └── Receipt chain: every crossing logged
│
├── Synth Origin (synth/index.html — Iteration 10 v67)
│   ├── Master control eye at universe center
│   ├── Scanner sweep detects civilisation contacts
│   ├── Signal/route network — communication backbone
│   ├── ARC authority receipts (GRANT/DENY/PING)
│   ├── SYNTH_UNIVERSE_FEED() — receives universe state
│   └── SYNTH_EMIT() — sends signal events to universe
│
└── ARC-Core (ARC_Console/)
    ├── Universe record ledger
    ├── Receipt chain (tamper-evident)
    ├── Branch simulation
    └── REST API: /api/universe/records
```

---

## Author
Gary Doman — DOMAN_ORIGIN_RECORD
Master Control: SURE v16 + Synth Origin v67 + ARC-Core + Bridge v1
