from __future__ import annotations

import math

import numpy as np
import pandas as pd


def _spearman(left: pd.Series, right: pd.Series) -> float:
    if len(left) < 2 or left.nunique() < 2 or right.nunique() < 2:
        return float("nan")
    return float(left.rank(method="average").corr(right.rank(method="average")))


def evaluate_predictions(
    frame: pd.DataFrame,
    prediction_column: str = "predicted_excess_return_90d",
    realized_column: str = "realized_excess_return_90d",
    probability_column: str | None = None,
) -> dict[str, float | int | None]:
    clean = frame.dropna(subset=[prediction_column, realized_column]).copy()
    if clean.empty:
        raise ValueError("no complete predictions to evaluate")
    predicted = clean[prediction_column].astype(float)
    realized = clean[realized_column].astype(float)
    prediction_has_rank = predicted.nunique() > 1
    bucket_size = max(1, math.ceil(len(clean) * 0.1))
    ranked = clean.sort_values(prediction_column)
    bottom = float(ranked.head(bucket_size)[realized_column].mean()) if prediction_has_rank else None
    top = float(ranked.tail(bucket_size)[realized_column].mean()) if prediction_has_rank else None
    result: dict[str, float | int | None] = {
        "n": int(len(clean)),
        "mae": float(np.mean(np.abs(predicted - realized))),
        "directional_hit_rate": float(np.mean((predicted > 0) == (realized > 0))),
        "spearman_rank_ic": _spearman(predicted, realized) if prediction_has_rank else None,
        "top_decile_realized_excess_return": top,
        "bottom_decile_realized_excess_return": bottom,
        "top_minus_bottom_spread": float(top - bottom) if top is not None and bottom is not None else None,
    }
    if probability_column and probability_column in clean:
        probability = clean[probability_column].clip(0, 1).astype(float)
        outcome = (realized > 0).astype(float)
        result["brier_score"] = float(np.mean((probability - outcome) ** 2))
        result["mean_probability"] = float(probability.mean())
        result["observed_outperformance_rate"] = float(outcome.mean())
    return result


def evaluate_by_cohort(frame: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for timestamp, cohort in frame.groupby("prediction_timestamp"):
        metrics = evaluate_predictions(cohort)
        metrics["prediction_timestamp"] = timestamp
        rows.append(metrics)
    return pd.DataFrame(rows).sort_values("prediction_timestamp")
