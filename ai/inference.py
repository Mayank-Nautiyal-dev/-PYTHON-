"""Inference entrypoint placeholder."""


def predict_next_load(features: list[float]) -> dict:
    baseline = sum(features) / len(features) if features else 0.0
    return {"predicted_load": round(baseline, 2), "confidence": 0.85}
