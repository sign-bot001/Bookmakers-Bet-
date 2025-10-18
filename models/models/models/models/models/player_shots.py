from .elo import poisson_tail

def expected_player_shots(shots90, minutes_expected=85, team_multiplier=1.0, role_multiplier=1.0):
    return shots90 * (minutes_expected/90.0) * team_multiplier * role_multiplier

def player_shots_probs(shots90, line=1.5, minutes_expected=85, team_multiplier=1.0, role_multiplier=1.0):
    lam = expected_player_shots(shots90, minutes_expected, team_multiplier, role_multiplier)
    k_threshold = int(line - 0.5)
    p_over = poisson_tail(lam, k_threshold)
    return p_over, 1 - p_over, lam
