"""PyPSA optimizer adapter."""


def run_opf(model_path: str) -> dict:
    """Return a mock OPF output until PyPSA model is connected."""
    return {
        "model": model_path,
        "dispatch_plan": [
            {"generator": "G1", "mw": 120.0},
            {"generator": "G2", "mw": 95.0},
        ],
        "objective_value": 15320.42,
    }
