"""Composite blackout risk score."""


def risk_score(load_risk: float, anomaly_score: float, voltage_deviation: float) -> float:
    return (load_risk * 0.5) + (anomaly_score * 0.3) + (voltage_deviation * 0.2)
