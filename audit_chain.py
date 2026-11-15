import hashlib
import json
import sqlite3
import time
GENESIS_HASH = "0" * 64
def init_db(db_path="sdpap_audit.db"):
conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS audit_log (
sequence INTEGER PRIMARY KEY AUTOINCREMENT,
state_version INTEGER NOT NULL,
timestamp REAL NOT NULL,
hypothesis_id TEXT NOT NULL,
observation_data TEXT NOT NULL,
evaluation_result TEXT NOT NULL,
prev_hash TEXT NOT NULL,
event_hash TEXT NOT NULL,
key_id TEXT,
signature_hex TEXT
);
""")
cur.execute("""
CREATE TRIGGER IF NOT EXISTS trg_prevent_update
BEFORE UPDATE ON audit_log
BEGIN SELECT RAISE(ABORT, 'append-only: update forbidden'); END;
""")
cur.execute("""
CREATE TRIGGER IF NOT EXISTS trg_prevent_delete
BEFORE DELETE ON audit_log
BEGIN SELECT RAISE(ABORT, 'append-only: delete forbidden'); END;
""")
conn.commit()
return conn
def compute_hash(envelope: dict) -> str:
canonical = json.dumps(envelope, sort_keys=True, separators=(',', ':')).encode('utf-8')
return hashlib.sha256(canonical).hexdigest()
def append_event(conn, state_version: int, hypothesis_id: str, obs: dict, eval_res: str):
cur = conn.cursor()
cur.execute("SELECT event_hash FROM audit_log ORDER BY sequence DESC LIMIT 1")
row = cur.fetchone()
prev_hash = row[0] if row else GENESIS_HASH
ts = time.time()
envelope = {
"state_version": state_version,
"timestamp": ts,
"hypothesis_id": hypothesis_id,
"observation_data": json.dumps(obs, sort_keys=True),
"evaluation_result": eval_res,
"prev_hash": prev_hash
}
event_hash = compute_hash(envelope)
cur.execute("""
INSERT INTO audit_log (state_version, timestamp, hypothesis_id, observation_data, evaluation_result, prev_hash, event_hash)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", (state_version, ts, hypothesis_id, envelope["observation_data"], eval_res, prev_hash, event_hash))
conn.commit()
return event_hash
def verify_full_integrity(conn) -> bool:
cur = conn.cursor()
cur.execute("SELECT sequence, state_version, timestamp, hypothesis_id, observation_data, evaluation_result, prev_hash, event_hash FROM audit_log ORDER BY sequence ASC")
expected_prev = GENESIS_HASH
for row in cur.fetchall():
seq, s_ver, ts, h_id, obs, ev_res, prev_h, ev_h = row
if prev_h != expected_prev:
return False
envelope = {
"state_version": s_ver,
"timestamp": ts,
"hypothesis_id": h_id,
"observation_data": obs,
"evaluation_result": ev_res,
"prev_hash": prev_h
}
if compute_hash(envelope) != ev_h:
return False
expected_prev = ev_h
return True
if name == "main":
db = init_db(":memory:")
h1 = append_event(db, 1, "SDPAP-V3-INIT", {"cell": "1T1R", "stack": "TiN/HfO2/TiO2/Ti/TiN"}, "PRIOR_ART_LOCKED")
print(f"Genesis Event Hash: {h1}")
print(f"Chain Integrity Valid: {verify_full_integrity(db)}")
