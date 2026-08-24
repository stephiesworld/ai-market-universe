# Synthetic example output

This example is an engineering acceptance test. It uses deterministic synthetic prices to exercise the complete pipeline and is not evidence of predictability in public markets.

## Run

```bash
market-universe demo --output-dir artifacts/demo
```

The command produces:

| Artifact | Purpose |
| --- | --- |
| `demo_research_frame.csv` | Point-in-time price features joined to forward labels. |
| `demo_predictions.csv` | Held-out predictions for each transparent baseline. |
| `demo_metrics.json` | Aggregate metrics and evidence-track labels. |
| `demo_forecasts.sqlite3` | Five immutable structured fixture forecasts. |
| `demo_forecast_manifest.json` | SHA-256 hashes for verifying stored payloads. |

## Example evaluation summary

The deterministic fixture currently yields 90 held-out observations:

| Model | MAE | Directional hit rate | Spearman rank IC | Top-minus-bottom spread |
| --- | ---: | ---: | ---: | ---: |
| Zero excess | 4.89% | 42.22% | Undefined | Undefined |
| 60-day momentum | 7.27% | 54.44% | 0.126 | 0.95% |
| Ridge | 5.12% | 55.56% | -0.167 | -2.53% |

Undefined ranking metrics for the zero baseline are intentional: identical predictions cannot create a meaningful ordering.

The negative held-out ridge rank IC is retained rather than hidden. The harness is designed to make null or adverse results visible. Because the generator is synthetic, none of these values should be compared with real strategies or cited as market performance.

## Explicit missingness

The stored fixture forecasts include registered vendor-dependent features even though no historical vendor is connected:

```json
{
  "consensus_eps": {
    "value": null,
    "available": false,
    "missing_reason": "no historical point-in-time vendor record connected",
    "provenance": {
      "as_of": "2024-01-29T00:00:00Z",
      "source": null,
      "published_at": null,
      "point_in_time_verified": true
    }
  }
}
```

This state is distinct from an observed consensus value of `0.0`.

## Evidence labeling

Every generated record is labeled `synthetic_fixture`, and the SQLite database is locked to that evidence track. It cannot accept `historical_backtest` or `prospective_live_paper` records.
