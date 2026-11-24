"""Inspector oficial de peajes, cargos BOE 2026 y breakeven tp/tep para tarifas 3.0TD y 6.1TD."""

from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    cfg = json.loads((Path(__file__).resolve().parent / "tariffs_2026.json").read_text(encoding="utf-8"))
    print(f"Año regulatorio: {cfg['year']} | IEE: {cfg['regulation']['iee_percent']}%")
    print(f"Normativa: {cfg['regulation']['peajes']} + {cfg['regulation']['cargos']}\n")
    for tariff_code in ("3.0TD", "6.1TD"):
        t = cfg["tariffs"][tariff_code]
        print(f"=== {t['label']} ===")
        for idx in range(6):
            tp = t["tp_eur_kw_year"][idx]
            tep_t13 = t["tep_t1_3_eur_kw"][idx]
            tep_t45 = t["tep_t4_5_eur_kw_day"][idx] if t["tep_t4_5_eur_kw_day"] else None
            be_days = f" | Breakeven T4-5: {tp / tep_t45:.1f} d/año" if tep_t45 else ""
            t45_str = f" | Exc. T4-5: {tep_t45:.6f} €/kW·d" if tep_t45 else ""
            print(f"  P{idx + 1}: Fijo {tp:.6f} €/kW·año | Exc. T1-3: {tep_t13:.6f} €/kW{t45_str}{be_days}")
        print()


if __name__ == "__main__":
    main()
