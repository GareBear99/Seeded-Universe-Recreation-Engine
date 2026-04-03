
from __future__ import annotations
import json
from arc.core.db import connect
from arc.core.schemas import UniverseRecordIn, new_id, utcnow
from arc.services.audit import append_receipt


def create_universe_record(item: UniverseRecordIn, actor_role: str = "system") -> dict:
    record_id = new_id("uni")
    created_at = utcnow()
    payload = item.dict()
    with connect() as conn:
        conn.execute(
            "INSERT INTO universe_records (record_id, record_type, seed, timeline_tick, scope_id, parent_scope_id, payload_json, solver_version, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                record_id,
                item.record_type,
                item.seed,
                item.timeline_tick,
                item.scope_id,
                item.parent_scope_id,
                json.dumps(item.payload, sort_keys=True),
                item.solver_version,
                created_at,
            ),
        )
        conn.commit()
    receipt = append_receipt("universe_record", record_id, actor_role, {
        "record_type": item.record_type,
        "seed": item.seed,
        "timeline_tick": item.timeline_tick,
        "scope_id": item.scope_id,
        "parent_scope_id": item.parent_scope_id,
        "solver_version": item.solver_version,
        "payload": item.payload,
    })
    return {
        "record_id": record_id,
        "record_type": item.record_type,
        "seed": item.seed,
        "timeline_tick": item.timeline_tick,
        "scope_id": item.scope_id,
        "parent_scope_id": item.parent_scope_id,
        "solver_version": item.solver_version,
        "payload": item.payload,
        "created_at": created_at,
        "receipt": receipt,
    }


def list_universe_records(seed: str | None = None, scope_id: str | None = None, limit: int = 100) -> list[dict]:
    query = "SELECT * FROM universe_records"
    clauses = []
    params = []
    if seed:
        clauses.append("seed = ?")
        params.append(seed)
    if scope_id:
        clauses.append("scope_id = ?")
        params.append(scope_id)
    if clauses:
        query += " WHERE " + " AND ".join(clauses)
    query += " ORDER BY created_at DESC LIMIT ?"
    params.append(limit)
    with connect() as conn:
        rows = conn.execute(query, tuple(params)).fetchall()
    return [{**dict(r), "payload": json.loads(r["payload_json"])} for r in rows]
