from risk.blackout_probability import risk_score
from risk.overload_model import overload_index


def test_overload_index():
    assert overload_index(450, 500) == 0.9


def test_risk_score():
    assert round(risk_score(0.9, 0.2, 0.1), 2) == 0.53
