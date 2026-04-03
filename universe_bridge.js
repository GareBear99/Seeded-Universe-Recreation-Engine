/**
 * UNIVERSE BRIDGE v1
 * The synth sits at the center of the universe.
 * This bridge feeds universe state into the synth and reads synth outputs back.
 *
 * Doctrine (TT-101):
 *   - Synth receives universe data — it does NOT generate it
 *   - Synth scanner detects civilisations — it does NOT create them
 *   - Synth signals propagate through universe physics — c_sim limit always applies
 *   - Every bridge event is logged as a receipt
 */

(function() {
  'use strict';

  // ── State ─────────────────────────────────────────────────────────────────
  const BRIDGE = {
    version: 'UNIVERSE_BRIDGE_v1',
    universeFrame: null,   // iframe or null if same-page
    synthFrame: null,
    lastUniverseState: null,
    receipts: [],
    tick: 0,
    online: false,
  };

  // ── Receipt logger ────────────────────────────────────────────────────────
  function receipt(event, data) {
    const r = { t: BRIDGE.tick, event, data, ts: Date.now() };
    BRIDGE.receipts.push(r);
    if (BRIDGE.receipts.length > 512) BRIDGE.receipts.shift();
    if (window.ARC_BRIDGE_LOG) window.ARC_BRIDGE_LOG(r);
    return r;
  }

  // ── Universe → Synth feed ─────────────────────────────────────────────────
  // Called when universe engine posts new state
  function onUniverseState(state) {
    BRIDGE.lastUniverseState = state;
    BRIDGE.tick++;

    // Extract civilisations within scanner range of universe center
    const civContacts = extractCivContacts(state);

    // Feed into synth as external contacts
    if (window.SYNTH_UNIVERSE_FEED) {
      window.SYNTH_UNIVERSE_FEED({
        tick: BRIDGE.tick,
        seed: state.seed,
        age: state.age,
        civContacts,
        lifeCapableCount: state.lifeCapableCount || 0,
        biosphereCount: state.biosphereCount || 0,
        snovaCount: state.snovaCount || 0,
        energyDelta: state.energyDelta || 0,
      });
    }

    receipt('universe_state_received', { seed: state.seed, age: state.age, civContacts: civContacts.length });
  }

  // ── Extract civ contacts from universe state ──────────────────────────────
  function extractCivContacts(state) {
    if (!state || !state.galaxies) return [];
    const contacts = [];
    for (const g of state.galaxies) {
      for (const s of g.stars || []) {
        for (const p of s.planets || []) {
          if (!p.biosphere) continue;
          const stage = p.biosphere.stage;
          const isActive = stage === 'complex' || stage === 'ecological';
          const score = p.biosphere.biosphereScore || 0;
          if (score > 0.35 || isActive) {
            // Distance from universe center (x,y of star)
            const dist = Math.hypot(s.x || 0, s.y || 0);
            contacts.push({
              id: p.id,
              starId: s.id,
              x: s.x || 0,
              y: s.y || 0,
              dist,
              stage,
              score,
              lifeCapable: p.lifeCapable || false,
              intelScore: p._intelScore || score * 0.8,
              tempK: p.tempK || 0,
              pressureBar: p.pressureBar || 0,
              hasSea: p.hasSea || false,
              // Signal strength decays with distance
              signalStrength: Math.max(0, 1 - dist / 600),
            });
          }
        }
      }
    }
    // Sort by signal strength (nearest first)
    contacts.sort((a, b) => b.signalStrength - a.signalStrength);
    return contacts.slice(0, 32);
  }

  // ── Synth → Universe output ───────────────────────────────────────────────
  // Called when synth produces a signal event (ping grant, contact mapped, etc.)
  function onSynthOutput(event) {
    receipt('synth_output', event);

    // If synth grants a CONTACT signal, inject into universe signal propagation
    if (event.type === 'contact_detected' && window.UNIVERSE_RECEIVE_SIGNAL) {
      window.UNIVERSE_RECEIVE_SIGNAL({
        source: 'synth_center',
        target: event.contactId,
        intelScore: event.intelScore || 0.5,
        tick: BRIDGE.tick,
        receipt: receipt('signal_injected', { contactId: event.contactId }),
      });
    }
  }

  // ── Synth universe blueprint ──────────────────────────────────────────────
  // Special blueprint that makes the synth's octagon represent the universe structure
  // Pivots map to galactic arms; rooms map to habitable zones
  function generateUniverseBlueprint(seed, galaxyCount) {
    const n = Math.max(3, Math.min(12, galaxyCount || 5));
    const pivots = [];
    const edges = [];
    for (let i = 0; i < n; i++) {
      const angle = (i / n) * Math.PI * 2;
      pivots.push({ id: i, u: Math.cos(angle) * 0.13, v: Math.sin(angle) * 0.13 });
      edges.push({ a: i, b: (i + 1) % n });
    }
    // Cross-connect alternate pivots (galactic filaments)
    for (let i = 0; i < n; i += 2) {
      edges.push({ a: i, b: (i + Math.floor(n / 2)) % n });
    }
    return {
      shellId: `UNIVERSE_SHELL_${seed}`,
      origin: { x: 0, y: 0, z: 1 },
      pivots,
      edges,
      rules: { perimeterFirst: true, mustValidateAll: true },
      rooms: [{
        id: 'cosmic-core',
        material: 'synth-space',
        pivots: [
          { u: 0.04, v: 0 }, { u: 0, v: 0.04 },
          { u: -0.04, v: 0 }, { u: 0, v: -0.04 },
        ]
      }],
      doors: [],
      _universe: true,
      _seed: seed,
      _galaxyCount: n,
    };
  }

  // ── Synth universe scanner module ─────────────────────────────────────────
  // Scanner tuned for intelligence detection rather than room mapping
  function generateUniverseScannerModule() {
    return {
      moduleType: 'scanner',
      id: 'UNIVERSE_INTELLIGENCE_SCANNER',
      style: 'iteration4',
      config: {
        label: 'INTELLIGENCE SCANNER',
        probeGlow: 1.4,
        sweepSpeed: 0.04,       // slower — cosmic scale
        sweepWidth: 0.015,
        contactPersistence: 2.5, // contacts persist longer
        sweepGlow: 0.28,
        _universeMode: true,
        _intelThreshold: 0.35,
      }
    };
  }

  // ── Synth ship module — Master Control Eye of the Universe ────────────────
  function generateUniverseShipModule() {
    return {
      moduleType: 'ship',
      id: 'UNIVERSE_MASTER_EYE',
      style: 'iteration4',
      config: {
        label: 'UNIVERSE ORIGIN',
        glow: 1.45,
        irisAspect: 0.92,
        slitBias: 1.12,
        _universeMode: true,
      }
    };
  }

  // ── Public API ────────────────────────────────────────────────────────────
  window.UNIVERSE_BRIDGE = {
    onUniverseState,
    onSynthOutput,
    generateUniverseBlueprint,
    generateUniverseScannerModule,
    generateUniverseShipModule,
    getReceipts: () => [...BRIDGE.receipts],
    getLastState: () => BRIDGE.lastUniverseState,
    getTick: () => BRIDGE.tick,
    version: BRIDGE.version,
  };

  // ── Auto-wire when both pages share a window ──────────────────────────────
  window.addEventListener('message', (ev) => {
    if (!ev.data || typeof ev.data !== 'object') return;
    if (ev.data.type === 'UNIVERSE_STATE') onUniverseState(ev.data.payload);
    if (ev.data.type === 'SYNTH_OUTPUT')   onSynthOutput(ev.data.payload);
  });

  console.log('[UNIVERSE_BRIDGE] v1 loaded — synth at the center of the universe');
})();
