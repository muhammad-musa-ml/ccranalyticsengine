"""Independent numerical checks for the simplified SA-CCR implementation."""

import math
import unittest

from ccranalytics.calculator.python.saccr_calculator import (
    SACCRCalculator,
    SACCRInput,
)


def fx_trade(mtm: float = 80.0) -> dict:
    return {"asset_class": "fx", "notional": 1000.0, "maturity": 1.0,
            "mtm": mtm, "delta": 1.0}


class SACCRFormulaTests(unittest.TestCase):
    def test_calculator_can_be_instantiated_and_tracks_calculations(self):
        calculator = SACCRCalculator()
        result = calculator.calculate(SACCRInput(trades=[fx_trade()]))
        self.assertGreater(result.ead, 0)
        self.assertEqual(calculator.calculation_count, 1)

    def test_margined_replacement_cost_uses_max_not_sum(self):
        # CRE52.18: V=80, NICA=20, VM=10, TH=5, MTA=2.
        data = SACCRInput(trades=[fx_trade()], collateral=20,
                          variation_margin=10, threshold=5,
                          minimum_transfer_amount=2, is_margined=True)
        self.assertEqual(SACCRCalculator().calculate(data).replacement_cost, 50)

    def test_variation_margin_is_part_of_net_collateral(self):
        data = SACCRInput(trades=[fx_trade(100)], collateral=0,
                          variation_margin=100, threshold=5,
                          is_margined=True)
        self.assertEqual(SACCRCalculator().calculate(data).replacement_cost, 5)

    def test_multiplier_uses_unfloored_market_value_less_collateral(self):
        data = SACCRInput(trades=[fx_trade(-20)], is_margined=False)
        result = SACCRCalculator().calculate(data)
        addon = 0.04 * 1000.0
        expected = 0.05 + 0.95 * math.exp(-20 / (2 * 0.95 * addon))
        self.assertAlmostEqual(result.multiplier, expected)
        self.assertAlmostEqual(result.ead, 1.4 * expected * addon)

    def test_margined_maturity_factor_has_basel_prefactor(self):
        data = SACCRInput(trades=[fx_trade()], is_margined=True,
                          margin_period_of_risk=10)
        result = SACCRCalculator().calculate(data)
        self.assertAlmostEqual(result.fx_addon,
                               0.04 * 1000 * 1.5 * math.sqrt(10 / 250))

    def test_unmargined_maturity_has_ten_business_day_floor(self):
        data = SACCRInput(trades=[dict(fx_trade(), maturity=0.001)])
        result = SACCRCalculator().calculate(data)
        self.assertAlmostEqual(result.fx_addon, 0.04 * 1000 * math.sqrt(10 / 250))

    def test_invalid_margin_inputs_rejected(self):
        with self.assertRaises(ValueError):
            SACCRCalculator().calculate(SACCRInput(margin_period_of_risk=0))
        with self.assertRaises(ValueError):
            SACCRCalculator().calculate(SACCRInput(collateral=float("nan")))


if __name__ == "__main__":
    unittest.main()
