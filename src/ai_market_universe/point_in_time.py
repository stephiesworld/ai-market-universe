from __future__ import annotations

from datetime import datetime

import pandas as pd


REQUIRED_AVAILABILITY_COLUMNS = {
    "ticker",
    "value",
    "published_at",
    "effective_at",
    "available_at",
    "ingested_at",
    "source",
    "source_record_id",
}


class PointInTimeError(ValueError):
    """Raised when a dataset violates the information clock."""


def normalize_timestamps(frame: pd.DataFrame) -> pd.DataFrame:
    result = frame.copy()
    for column in ("published_at", "effective_at", "available_at", "ingested_at"):
        if column in result:
            result[column] = pd.to_datetime(result[column], utc=True)
    return result


def validate_long_records(frame: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED_AVAILABILITY_COLUMNS - set(frame.columns)
    if missing:
        raise PointInTimeError(f"missing point-in-time columns: {sorted(missing)}")
    result = normalize_timestamps(frame)
    if result["source_record_id"].duplicated().any():
        duplicates = result.loc[result["source_record_id"].duplicated(), "source_record_id"].tolist()
        raise PointInTimeError(f"duplicate source record ids: {duplicates[:5]}")
    return result


def as_of(frame: pd.DataFrame, timestamp: datetime, key_columns: tuple[str, ...]) -> pd.DataFrame:
    """Return the latest record per key that was actually available by timestamp."""
    data = validate_long_records(frame)
    cutoff = pd.Timestamp(timestamp)
    cutoff = cutoff.tz_localize("UTC") if cutoff.tzinfo is None else cutoff.tz_convert("UTC")
    eligible = data.loc[data["available_at"] <= cutoff].copy()
    if eligible.empty:
        return eligible
    eligible = eligible.sort_values([*key_columns, "available_at", "ingested_at"])
    return eligible.groupby(list(key_columns), as_index=False, sort=False).tail(1)


def assert_no_future_information(frame: pd.DataFrame) -> None:
    required = {"prediction_timestamp", "available_at"}
    if not required.issubset(frame.columns):
        raise PointInTimeError(f"missing columns: {sorted(required - set(frame.columns))}")
    prediction = pd.to_datetime(frame["prediction_timestamp"], utc=True)
    available = pd.to_datetime(frame["available_at"], utc=True)
    bad = frame.loc[available > prediction]
    if not bad.empty:
        raise PointInTimeError(f"{len(bad)} rows contain future information")
