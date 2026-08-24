from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Protocol

import pandas as pd

from .point_in_time import as_of, validate_long_records


class PointInTimeProvider(Protocol):
    def observations_as_of(self, timestamp: datetime) -> pd.DataFrame: ...


class CsvPointInTimeProvider:
    """Vendor-neutral adapter for long-form records with explicit availability clocks."""

    def __init__(self, path: str | Path, key_columns: tuple[str, ...] = ("ticker", "field")):
        self.path = Path(path)
        self.key_columns = key_columns

    def observations_as_of(self, timestamp: datetime) -> pd.DataFrame:
        data = validate_long_records(pd.read_csv(self.path))
        return as_of(data, timestamp, self.key_columns)
