from __future__ import annotations

from datetime import datetime

import numpy as np
import pandas as pd


def _utc(value: datetime | str | pd.Timestamp) -> pd.Timestamp:
    result = pd.Timestamp(value)
    return result.tz_localize("UTC") if result.tzinfo is None else result.tz_convert("UTC")


def _price_before(series: pd.DataFrame, timestamp: pd.Timestamp) -> tuple[pd.Timestamp, float]:
    eligible = series.loc[series["timestamp"] <= timestamp]
    if eligible.empty:
        raise ValueError(f"no price at or before {timestamp}")
    row = eligible.iloc[-1]
    return row["timestamp"], float(row["adjusted_close"])


def _price_after(series: pd.DataFrame, timestamp: pd.Timestamp) -> tuple[pd.Timestamp, float]:
    eligible = series.loc[series["timestamp"] >= timestamp]
    if eligible.empty:
        raise ValueError(f"no price at or after {timestamp}")
    row = eligible.iloc[0]
    return row["timestamp"], float(row["adjusted_close"])


def generate_forward_labels(
    prices: pd.DataFrame,
    observations: pd.DataFrame,
    horizons: tuple[int, ...] = (7, 30, 60, 90),
    benchmark: str = "SPY",
) -> pd.DataFrame:
    """Generate calendar-day returns, snapping endpoints to observable trading closes."""
    data = prices.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"], utc=True)
    data = data.sort_values(["ticker", "timestamp"])
    grouped = {ticker: group.reset_index(drop=True) for ticker, group in data.groupby("ticker")}
    if benchmark not in grouped:
        raise ValueError(f"benchmark {benchmark} is missing")

    rows: list[dict[str, object]] = []
    for observation in observations.itertuples(index=False):
        ticker = observation.ticker
        start = _utc(observation.prediction_timestamp)
        stock = grouped[ticker]
        bench = grouped[benchmark]
        stock_start_date, stock_start = _price_before(stock, start)
        bench_start_date, bench_start = _price_before(bench, start)
        row: dict[str, object] = {
            "ticker": ticker,
            "prediction_timestamp": start,
            "stock_start_timestamp": stock_start_date,
            "benchmark_start_timestamp": bench_start_date,
            "price_day_0": stock_start,
            "benchmark_day_0": bench_start,
        }
        for horizon in horizons:
            target = start + pd.Timedelta(days=horizon)
            end_date, stock_end = _price_after(stock, target)
            bench_end_date, bench_end = _price_after(bench, target)
            stock_return = stock_end / stock_start - 1
            benchmark_return = bench_end / bench_start - 1
            path = stock.loc[(stock["timestamp"] > stock_start_date) & (stock["timestamp"] <= end_date), "adjusted_close"]
            wealth = pd.concat([pd.Series([stock_start]), path], ignore_index=True)
            drawdown = wealth / wealth.cummax() - 1
            row.update(
                {
                    f"realized_return_{horizon}d": stock_return,
                    f"benchmark_return_{horizon}d": benchmark_return,
                    f"realized_excess_return_{horizon}d": stock_return - benchmark_return,
                    f"max_drawdown_{horizon}d": float(drawdown.min()),
                    f"realization_timestamp_{horizon}d": max(end_date, bench_end_date),
                }
            )
        rows.append(row)
    return pd.DataFrame(rows)
