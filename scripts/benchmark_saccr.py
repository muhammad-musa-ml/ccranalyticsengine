"""Reproduce before/after SA-CCR formula errors on deterministic toy netting sets.

Run from the repository root: python -m scripts.benchmark_saccr
No market data or calibrated risk model is implied by these synthetic examples.
"""

import csv
import math
from pathlib import Path

from ccranalytics.calculator.python.saccr_calculator import SACCRCalculator, SACCRInput


OUT = Path(__file__).resolve().parents[1] / "evidence"


def trade(mtm):
    return {"asset_class": "fx", "notional": 1000.0, "maturity": 1.0,
            "mtm": mtm, "delta": 1.0}


CASES = {
    "threshold + VM": SACCRInput(trades=[trade(100)], threshold=5,
                                   variation_margin=100, is_margined=True),
    "NICA + VM": SACCRInput(trades=[trade(80)], collateral=20,
                              variation_margin=10, threshold=5,
                              minimum_transfer_amount=2, is_margined=True),
    "overcollateral": SACCRInput(trades=[trade(80)], collateral=150,
                                 variation_margin=50,
                                 minimum_transfer_amount=5, is_margined=True),
    "negative MTM": SACCRInput(trades=[trade(-20)]),
    "unmargined": SACCRInput(trades=[trade(80)], collateral=20),
}


def multiplier(v_minus_c, addon):
    if addon == 0:
        return 1.0
    return min(1.0, 0.05 + 0.95 * math.exp(v_minus_c / (2 * 0.95 * addon)))


def legacy_ead(data):
    """Original repository's three formulas, transcribed before the correction."""
    v = sum(t["mtm"] for t in data.trades)
    nica = data.collateral
    if data.is_margined:
        rc = max(0, v - nica) + max(
            0, data.threshold + data.minimum_transfer_amount - data.variation_margin)
        mf = min(1.0, math.sqrt(data.margin_period_of_risk / 250))
    else:
        rc = max(0, v - nica)
        mf = 1.0
    addon = 0.04 * 1000 * mf
    return 1.4 * (rc + multiplier(rc - nica, addon) * addon)


def basel_reference_ead(data):
    """Independent scalar CRE52.18/.23/.52 reference for one FX trade."""
    v = data.trades[0]["mtm"]
    nica = data.collateral
    c = nica + (data.variation_margin if data.is_margined else 0)
    rc = (max(v - c, data.threshold + data.minimum_transfer_amount - nica, 0)
          if data.is_margined else max(v - c, 0))
    mf = (1.5 * math.sqrt(data.margin_period_of_risk / 250)
          if data.is_margined else 1.0)
    addon = 0.04 * 1000 * mf
    return 1.4 * (rc + multiplier(v - c, addon) * addon)


def write_svg(rows):
    width, height, left, top, plot_h = 850, 400, 72, 46, 270
    max_error = max(row["legacy_abs_error"] for row in rows)
    scale = plot_h / max_error
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<text x="425" y="25" text-anchor="middle" font-family="Arial" font-size="18">Absolute EAD error vs Basel formula reference</text>',
        f'<line x1="{left}" y1="{top+plot_h}" x2="810" y2="{top+plot_h}" stroke="#333"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" stroke="#333"/>',
    ]
    for tick in range(5):
        val = max_error * tick / 4
        y = top + plot_h - val * scale
        parts.append(f'<text x="65" y="{y+4:.1f}" text-anchor="end" font-family="Arial" font-size="11">{val:.0f}</text>')
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="810" y2="{y:.1f}" stroke="#eee"/>')
    for idx, row in enumerate(rows):
        x = left + 80 + idx * 145
        for offset, key, color in ((0, "legacy_abs_error", "#c75b39"),
                                   (37, "corrected_abs_error", "#237a68")):
            bar_h = row[key] * scale
            if bar_h == 0:
                # Zero-height bars disappear, so mark exact matches on the axis.
                parts.append(f'<circle cx="{x+offset+16.5:.1f}" cy="{top+plot_h-5}" r="5" fill="{color}"/>')
            else:
                parts.append(f'<rect x="{x+offset}" y="{top+plot_h-bar_h:.2f}" width="33" height="{bar_h:.2f}" fill="{color}"/>')
        parts.append(f'<text x="{x+17}" y="{top+plot_h+20}" text-anchor="middle" font-family="Arial" font-size="10">{row["case"]}</text>')
    parts += [
        '<rect x="310" y="366" width="14" height="12" fill="#c75b39"/><text x="330" y="377" font-family="Arial" font-size="12">Original</text>',
        '<rect x="430" y="366" width="14" height="12" fill="#237a68"/><text x="450" y="377" font-family="Arial" font-size="12">Corrected</text>',
        '<text x="425" y="394" text-anchor="middle" font-family="Arial" font-size="11">Dots on the axis mark zero error.</text>',
        '</svg>',
    ]
    (OUT / "saccr_error.svg").write_text("\n".join(parts), encoding="utf-8")


def main():
    OUT.mkdir(exist_ok=True)
    rows = []
    for name, data in CASES.items():
        old = legacy_ead(data)
        new = SACCRCalculator().calculate(data).ead
        reference = basel_reference_ead(data)
        rows.append({"case": name, "legacy_ead": old,
                     "corrected_ead": new, "reference_ead": reference,
                     "legacy_abs_error": abs(old-reference),
                     "corrected_abs_error": abs(new-reference)})
    with (OUT / "saccr_results.csv").open("w", newline="", encoding="utf-8") as out:
        writer = csv.DictWriter(out, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    write_svg(rows)
    for row in rows:
        print(f'{row["case"]}: old={row["legacy_ead"]:.4f}, '
              f'new={row["corrected_ead"]:.4f}, '
              f'reference={row["reference_ead"]:.4f}')


if __name__ == "__main__":
    main()
