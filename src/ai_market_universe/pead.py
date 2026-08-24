from __future__ import annotations

import numpy as np
import pandas as pd

from .point_in_time import PointInTimeError


def safe_surprise(actual: float | None, consensus: float | None) -> float:
    if actual is None or consensus is None or not np.isfinite(actual) or not np.isfinite(consensus):
        return float("nan")
    denominator = max(abs(consensus), 1e-9)
    return float((actual - consensus) / denominator)


def build_pead_event_features(events: pd.DataFrame, reactions: pd.DataFrame) -> pd.DataFrame:
    """Build one post-announcement observation per event without crossing the event clock."""
    required_event = {
        "event_id", "ticker", "announcement_timestamp", "prediction_timestamp",
        "available_at", "eps_actual", "eps_consensus", "revenue_actual", "revenue_consensus",
    }
    missing = required_event - set(events.columns)
    if missing:
        raise ValueError(f"missing earnings columns: {sorted(missing)}")
    event_data = events.copy()
    reaction_data = reactions.copy()
    for frame, columns in (
        (event_data, ("announcement_timestamp", "prediction_timestamp", "available_at")),
        (reaction_data, ("available_at",)),
    ):
        for column in columns:
            frame[column] = pd.to_datetime(frame[column], utc=True)
    if (event_data["available_at"] > event_data["prediction_timestamp"]).any():
        raise PointInTimeError("earnings data unavailable at PEAD prediction time")
    merged = event_data.merge(reaction_data, on=["event_id", "ticker"], suffixes=("", "_reaction"))
    if (merged["available_at_reaction"] > merged["prediction_timestamp"]).any():
        raise PointInTimeError("reaction feature unavailable at PEAD prediction time")
    merged["eps_surprise"] = [
        safe_surprise(actual, consensus)
        for actual, consensus in zip(merged["eps_actual"], merged["eps_consensus"])
    ]
    merged["revenue_surprise"] = [
        safe_surprise(actual, consensus)
        for actual, consensus in zip(merged["revenue_actual"], merged["revenue_consensus"])
    ]
    merged["surprise_reaction_gap"] = merged["eps_surprise"] - merged["earnings_day_abnormal_return"]
    return merged
