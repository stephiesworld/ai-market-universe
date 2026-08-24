from __future__ import annotations

import hashlib
import json
import sqlite3
from pathlib import Path

from .schemas import EvidenceTrack, Forecast


SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS store_metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS forecasts (
    evidence_track TEXT NOT NULL,
    cohort_id TEXT NOT NULL,
    ticker TEXT NOT NULL,
    prediction_timestamp TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    payload_sha256 TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (cohort_id, ticker)
);
CREATE TRIGGER IF NOT EXISTS forecasts_no_update
BEFORE UPDATE ON forecasts
BEGIN
    SELECT RAISE(ABORT, 'forecasts are immutable');
END;
CREATE TRIGGER IF NOT EXISTS forecasts_no_delete
BEFORE DELETE ON forecasts
BEGIN
    SELECT RAISE(ABORT, 'forecasts are immutable');
END;
"""


class ForecastStore:
    def __init__(self, path: str | Path, evidence_track: EvidenceTrack | str):
        self.path = Path(path)
        self.evidence_track = EvidenceTrack(evidence_track)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as connection:
            connection.executescript(SCHEMA)
            connection.execute(
                "INSERT OR IGNORE INTO store_metadata(key,value) VALUES ('evidence_track',?)",
                (self.evidence_track.value,),
            )
            stored = connection.execute(
                "SELECT value FROM store_metadata WHERE key='evidence_track'"
            ).fetchone()[0]
            if stored != self.evidence_track.value:
                raise ValueError(
                    f"store is locked to evidence track {stored}, not {self.evidence_track.value}"
                )

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)

    def append(self, forecast: Forecast) -> str:
        if forecast.evidence_track != self.evidence_track:
            raise ValueError(
                f"cannot write {forecast.evidence_track.value} into {self.evidence_track.value} store"
            )
        payload = forecast.model_dump_json()
        digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        with self.connect() as connection:
            connection.execute(
                "INSERT INTO forecasts(evidence_track,cohort_id,ticker,prediction_timestamp,payload_json,payload_sha256) VALUES (?,?,?,?,?,?)",
                (
                    forecast.evidence_track.value,
                    forecast.cohort_id,
                    forecast.ticker,
                    forecast.prediction_timestamp.isoformat(),
                    payload,
                    digest,
                ),
            )
        return digest

    def load(self, cohort_id: str, ticker: str) -> Forecast:
        with self.connect() as connection:
            row = connection.execute(
                "SELECT payload_json,payload_sha256 FROM forecasts WHERE cohort_id=? AND ticker=?",
                (cohort_id, ticker),
            ).fetchone()
        if row is None:
            raise KeyError((cohort_id, ticker))
        payload, digest = row
        actual = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        if actual != digest:
            raise RuntimeError("forecast payload hash mismatch")
        return Forecast.model_validate_json(payload)

    def manifest(self) -> list[dict[str, str]]:
        with self.connect() as connection:
            rows = connection.execute(
                "SELECT evidence_track,cohort_id,ticker,prediction_timestamp,payload_sha256 FROM forecasts ORDER BY cohort_id,ticker"
            ).fetchall()
        return [
            dict(
                zip(
                    ("evidence_track", "cohort_id", "ticker", "prediction_timestamp", "payload_sha256"),
                    row,
                )
            )
            for row in rows
        ]

    def export_manifest(self, path: str | Path) -> None:
        Path(path).write_text(json.dumps(self.manifest(), indent=2) + "\n", encoding="utf-8")
