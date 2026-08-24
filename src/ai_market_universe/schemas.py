from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator


class FrozenModel(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")


class EvidenceTrack(StrEnum):
    PROSPECTIVE_LIVE_PAPER = "prospective_live_paper"
    HISTORICAL_BACKTEST = "historical_backtest"
    SYNTHETIC_FIXTURE = "synthetic_fixture"


class Provenance(FrozenModel):
    as_of: datetime
    source: str | None = None
    source_record_id: str | None = None
    published_at: datetime | None = None
    effective_at: datetime | None = None
    available_at: datetime | None = None
    ingested_at: datetime | None = None
    point_in_time_verified: bool


class FeatureValue(FrozenModel):
    value: float | None
    available: bool
    provenance: Provenance
    missing_reason: str | None = None

    @model_validator(mode="after")
    def distinguish_missing_from_zero(self) -> "FeatureValue":
        if self.available:
            if self.value is None:
                raise ValueError("an available numeric feature must have a value; zero is valid")
            required = {
                "source": self.provenance.source,
                "source_record_id": self.provenance.source_record_id,
                "published_at": self.provenance.published_at,
                "available_at": self.provenance.available_at,
            }
            missing = [name for name, value in required.items() if value is None]
            if missing:
                raise ValueError(f"available feature is missing provenance: {missing}")
            if self.missing_reason is not None:
                raise ValueError("available feature cannot have a missing_reason")
        else:
            if self.value is not None:
                raise ValueError("unavailable feature value must be null, never zero-filled")
            if not self.missing_reason:
                raise ValueError("unavailable feature requires a missing_reason")
            forbidden = {
                "source": self.provenance.source,
                "source_record_id": self.provenance.source_record_id,
                "published_at": self.provenance.published_at,
                "effective_at": self.provenance.effective_at,
                "available_at": self.provenance.available_at,
            }
            present = [name for name, value in forbidden.items() if value is not None]
            if present:
                raise ValueError(f"unavailable feature must not invent provenance: {present}")
        return self


class FeatureSnapshot(FrozenModel):
    ticker: str
    prediction_timestamp: datetime
    feature_schema_version: str
    features: dict[str, FeatureValue]

    @model_validator(mode="after")
    def enforce_point_in_time(self) -> "FeatureSnapshot":
        future = [
            name
            for name, item in self.features.items()
            if item.provenance.available_at is not None
            and item.provenance.available_at > self.prediction_timestamp
        ]
        if future:
            raise ValueError(f"features unavailable at prediction time: {future}")
        wrong_as_of = [
            name
            for name, item in self.features.items()
            if item.provenance.as_of != self.prediction_timestamp
        ]
        if wrong_as_of:
            raise ValueError(f"feature as_of does not match prediction timestamp: {wrong_as_of}")
        return self

    def numeric_values(self, verified_only: bool = True) -> dict[str, float | None]:
        return {
            name: (
                item.value
                if item.available
                and (item.provenance.point_in_time_verified or not verified_only)
                else None
            )
            for name, item in self.features.items()
        }


class Forecast(FrozenModel):
    evidence_track: EvidenceTrack
    cohort_id: str
    ticker: str
    prediction_timestamp: datetime
    price_day_0: float = Field(gt=0)
    spy_day_0: float = Field(gt=0)
    predicted_return_90d: float
    predicted_excess_return_90d: float
    prob_outperform_spy: float = Field(ge=0, le=1)
    confidence: float = Field(ge=0, le=1)
    bull_case_return: float
    base_case_return: float
    bear_case_return: float
    consensus_view: str
    ai_view: str
    variant_perception: str
    thesis: str
    catalysts: tuple[str, ...] = ()
    risks: tuple[str, ...] = ()
    sector: str
    market_cap: float | None = Field(default=None, ge=0)
    earnings_date: datetime | None = None
    days_until_earnings: int | None = None
    model_version: str
    prompt_version: str
    feature_schema_version: str
    data_snapshot_version: str
    feature_snapshot: dict[str, Any]

    @model_validator(mode="after")
    def scenarios_are_ordered(self) -> "Forecast":
        if not self.bear_case_return <= self.base_case_return <= self.bull_case_return:
            raise ValueError("return scenarios must satisfy bear <= base <= bull")
        return self


class EarningsEvent(FrozenModel):
    ticker: str
    announcement_timestamp: datetime
    prediction_timestamp: datetime
    fiscal_period: str
    eps_actual: float | None = None
    eps_consensus: float | None = None
    revenue_actual: float | None = None
    revenue_consensus: float | None = None
    guidance_change: str | None = None
    provenance: Provenance

    @model_validator(mode="after")
    def validate_event_clock(self) -> "EarningsEvent":
        if self.provenance.available_at > self.prediction_timestamp:
            raise ValueError("earnings record was not available at prediction time")
        if self.prediction_timestamp < self.announcement_timestamp:
            raise ValueError("PEAD prediction cannot precede the announcement")
        return self
