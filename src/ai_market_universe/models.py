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
        values = frame["momentum_60d"].fillna(0.0).to_numpy(dtype=float)
        return values - np.nanmean(values)


@dataclass
class RidgeRegressor:
    alpha: float = 10.0
    name: str = "ridge_v1"

    def __post_init__(self) -> None:
        self.columns_: list[str] | None = None
        self.mean_: np.ndarray | None = None
        self.scale_: np.ndarray | None = None
        self.coef_: np.ndarray | None = None
        self.intercept_: float | None = None

    def fit(self, frame: pd.DataFrame, target: pd.Series, columns: list[str]) -> "RidgeRegressor":
        x = frame[columns].astype(float).copy()
        x = x.fillna(x.median()).fillna(0.0).to_numpy()
        y = target.to_numpy(dtype=float)
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
        x = frame[self.columns_].astype(float).copy()
        x = x.fillna(pd.Series(self.mean_, index=self.columns_)).fillna(0.0).to_numpy()
        z = (x - self.mean_) / self.scale_
        return self.intercept_ + z @ self.coef_


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
