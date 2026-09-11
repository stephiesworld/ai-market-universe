from __future__ import annotations

import unittest

import numpy as np
import pandas as pd

from ai_market_universe.models import MomentumBaseline, RidgeRegressor


def _complete_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "momentum_60d": [0.10, 0.20, -0.05, 0.00],
            "consensus_eps": [1.5, 2.0, 0.0, 1.1],
            "consensus_eps_available": [True, True, True, True],
        }
    )


class RidgeMissingnessTests(unittest.TestCase):
    def test_fit_refuses_null_consensus_instead_of_median_or_zero_fill(self) -> None:
        frame = _complete_frame()
        frame.loc[1, "consensus_eps"] = np.nan
        frame.loc[1, "consensus_eps_available"] = False
        target = pd.Series([0.01, 0.02, -0.01, 0.00])
        with self.assertRaises(ValueError) as raised:
            RidgeRegressor().fit(frame, target, ["momentum_60d", "consensus_eps"])
        message = str(raised.exception).lower()
        self.assertIn("not imputed", message)
        self.assertIn("consensus_eps", message)

    def test_missing_consensus_is_not_used_as_numeric_zero_at_predict(self) -> None:
        train = _complete_frame()
        target = pd.Series([0.04, 0.05, -0.02, 0.01])
        model = RidgeRegressor(alpha=1.0).fit(train, target, ["momentum_60d", "consensus_eps"])

        observed_zero = pd.DataFrame(
            {
                "momentum_60d": [0.10],
                "consensus_eps": [0.0],
                "consensus_eps_available": [True],
            }
        )
        missing_null = pd.DataFrame(
            {
                "momentum_60d": [0.10],
                "consensus_eps": [np.nan],
                "consensus_eps_available": [False],
            }
        )
        placeholder_zero = pd.DataFrame(
            {
                "momentum_60d": [0.10],
                "consensus_eps": [0.0],
                "consensus_eps_available": [False],
            }
        )

        observed_prediction = model.predict(observed_zero)
        self.assertEqual(observed_prediction.shape, (1,))
        self.assertFalse(np.isnan(observed_prediction).any())

        with self.assertRaises(ValueError) as missing:
            model.predict(missing_null)
        self.assertIn("not imputed", str(missing.exception).lower())

        with self.assertRaises(ValueError) as placeholder:
            model.predict(placeholder_zero)
        self.assertIn("consensus_eps", str(placeholder.exception))

    def test_observed_zero_consensus_is_distinct_from_absence(self) -> None:
        train = pd.DataFrame(
            {
                "consensus_eps": [0.0, 1.0, 2.0],
                "consensus_eps_available": [True, True, True],
            }
        )
        target = pd.Series([0.0, 0.1, 0.2])
        model = RidgeRegressor(alpha=0.1).fit(train, target, ["consensus_eps"])
        self.assertIsNotNone(model.coef_)
        self.assertFalse(np.isnan(model.coef_).any())
        prediction = model.predict(train.iloc[[0]])
        self.assertAlmostEqual(float(prediction[0]), 0.0, places=6)

    def test_momentum_baseline_does_not_zero_fill_missing_momentum(self) -> None:
        frame = pd.DataFrame({"momentum_60d": [0.1, np.nan, 0.2]})
        with self.assertRaises(ValueError) as raised:
            MomentumBaseline().predict(frame)
        self.assertIn("momentum_60d", str(raised.exception))
        self.assertIn("not imputed", str(raised.exception).lower())


if __name__ == "__main__":
    unittest.main()
