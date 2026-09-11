from __future__ import annotations

from datetime import datetime

import pandas as pd


def load_universe_as_of(path: str, timestamp: datetime) -> pd.DataFrame:
    """Resolve membership using effective dates to make survivorship assumptions explicit.

    Interval is half-open: a name is a member iff
    ``valid_from <= timestamp < valid_to``. Blank ``valid_to`` is open-ended
    (still a member on and after ``valid_from``). Names are never inferred;
    an as-of miss returns fewer rows rather than expanding the file's set.
    """
    universe = pd.read_csv(path, dtype={"ticker": str})
    required = {"ticker", "valid_from", "valid_to", "selection_rule"}
    missing = required - set(universe.columns)
    if missing:
        raise ValueError(f"missing universe columns: {sorted(missing)}")
    valid_from = pd.to_datetime(universe["valid_from"], utc=True)
    valid_to = pd.to_datetime(universe["valid_to"].replace(r"^\s*$", pd.NA, regex=True), utc=True, errors="coerce")
    cutoff = pd.Timestamp(timestamp)
    cutoff = cutoff.tz_localize("UTC") if cutoff.tzinfo is None else cutoff.tz_convert("UTC")
    selected = universe.loc[(valid_from <= cutoff) & (valid_to.isna() | (cutoff < valid_to))].copy()
    if selected["ticker"].duplicated().any():
        raise ValueError("universe contains overlapping membership windows")
    return selected.reset_index(drop=True)
