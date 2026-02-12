"""Contingency analysis utilities."""


def evaluate_n_minus_one(line_loadings: list[float], threshold: float = 90.0) -> dict:
    overloaded = [idx for idx, value in enumerate(line_loadings) if value > threshold]
    return {
        "threshold_pct": threshold,
        "violations": overloaded,
        "secure": len(overloaded) == 0,
    }
