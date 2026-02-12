"""Transformer model definition placeholder."""


def model_signature() -> dict:
    return {
        "name": "transformer",
        "layers": ["InputProjection", "Encoder x4", "Dense(1)"],
    }
