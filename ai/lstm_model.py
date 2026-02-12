"""LSTM model definition placeholder."""


def model_signature() -> dict:
    return {
        "name": "lstm",
        "layers": ["LSTM(128)", "Dropout(0.2)", "LSTM(64)", "Dense(1)"],
    }
