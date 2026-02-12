"""Overload risk calculations."""


def overload_index(predicted_load: float, transformer_capacity: float) -> float:
    if transformer_capacity <= 0:
        return 0.0
    return predicted_load / transformer_capacity
