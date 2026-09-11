from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


class ZeroExcessBaseline:
    name = "zero_excess_v1"

    def predict(self, frame: pd.DataFrame) -> np.ndarray:
        return np.zeros(len(frame), dtype=float)


class MomentumBaseline:
    name = "momentum_60d_v1"

    def predict(self, frame: pd.DataFrame) -> np.ndarray:
        values = _require_observed_matrix(frame, ["momentum_60d"]).reshape(-1)
        return values - values.mean()


@dataclass
class RidgeRegressor:
    """Centered ridge on observed numeric features only.

    Missingness contract:
    - Fit and predict never median-fill or zero-fill a missing feature.
    - NaN is unobserved. Companion ``{column}_available`` flags, when present,
      mark a row unobserved even if a placeholder such as ``0.0`` was stored.
    - An observed numeric zero remains valid when the value is non-null and
      any companion available flag is true.
    - Incomplete rows/features are refused; callers must drop them or omit
      the unobserved column rather than treating absence as a signal.
    """

    alpha: float = 10.0
    name: str = "ridge_v1"

    def __post_init__(self) -> None:
        self.columns_: list[str] | None = None
        self.mean_: np.ndarray | None = None
        self.scale_: np.ndarray | None = None
        self.coef_: np.ndarray | None = None
        self.intercept_: float | None = None

    def fit(self, frame: pd.DataFrame, target: pd.Series, columns: list[str]) -> "RidgeRegressor":
        x = _require_observed_matrix(frame, columns)
        y = target.to_numpy(dtype=float)
        if len(y) != len(x):
            raise ValueError("target length must match the feature frame")
        if np.isnan(y).any():
            raise ValueError("target values must be observed; missing labels are not imputed")
        self.columns_ = columns
        self.mean_ = x.mean(axis=0)
        self.scale_ = x.std(axis=0)
        self.scale_[self.scale_ == 0] = 1.0
        z = (x - self.mean_) / self.scale_
        self.intercept_ = float(y.mean())
        centered = y - self.intercept_
        penalty = self.alpha * np.eye(z.shape[1])
        self.coef_ = np.linalg.solve(z.T @ z + penalty, z.T @ centered)
        return self

    def predict(self, frame: pd.DataFrame) -> np.ndarray:
        if any(value is None for value in (self.columns_, self.mean_, self.scale_, self.coef_, self.intercept_)):
            raise RuntimeError("model must be fit before prediction")
        x = _require_observed_matrix(frame, self.columns_)
        z = (x - self.mean_) / self.scale_
        return self.intercept_ + z @ self.coef_


def _require_observed_matrix(frame: pd.DataFrame, columns: list[str]) -> np.ndarray:
    missing_columns = [name for name in columns if name not in frame.columns]
    if missing_columns:
        raise ValueError(f"missing feature columns: {missing_columns}")
    observed = pd.DataFrame(index=frame.index)
    unobserved: list[str] = []
    for name in columns:
        numeric = pd.to_numeric(frame[name], errors="coerce")
        available_name = f"{name}_available"
        if available_name in frame.columns:
            available = frame[available_name].fillna(False).astype(bool)
            numeric = numeric.where(available)
        if numeric.isna().any():
            unobserved.append(name)
        observed[name] = numeric
    if unobserved:
        raise ValueError(
            "missing features are not imputed with median or zero; "
            f"unobserved columns: {unobserved}. Pass only observed rows/features "
            "or explicit available flags that remain false for absent consensus."
        )
    return observed.to_numpy(dtype=float)


def temporal_split(
    frame: pd.DataFrame,
    train_end: str | pd.Timestamp,
    validation_end: str | pd.Timestamp,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    timestamps = pd.to_datetime(frame["prediction_timestamp"], utc=True)
    train_cut = pd.Timestamp(train_end)
    valid_cut = pd.Timestamp(validation_end)
    train_cut = train_cut.tz_localize("UTC") if train_cut.tzinfo is None else train_cut.tz_convert("UTC")
    valid_cut = valid_cut.tz_localize("UTC") if valid_cut.tzinfo is None else valid_cut.tz_convert("UTC")
    train = frame.loc[timestamps <= train_cut].copy()
    validation = frame.loc[(timestamps > train_cut) & (timestamps <= valid_cut)].copy()
    test = frame.loc[timestamps > valid_cut].copy()
    if train.empty or validation.empty or test.empty:
        raise ValueError("temporal split must produce non-empty train, validation, and test sets")
    return train, validation, test
