def kelly_fraction(p: float, odds: float) -> float:
    b = odds - 1.0
    edge = (odds * p - (1 - p)) / b if b>0 else 0.0
    return max(0.0, edge)

def capped_stake_pct(p: float, odds: float, kelly_frac_base: float, min_pct: float, max_pct: float) -> float:
    f_star = kelly_fraction(p, odds)
    stake = f_star * kelly_frac_base
    return max(min_pct, min(max_pct, stake))
