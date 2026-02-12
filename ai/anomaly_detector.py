"""Anomaly detection helpers."""

import statistics


def detect_spikes(series: list[float], z_threshold: float = 2.5) -> list[int]:
    if len(series) < 2:
        return []
    mean = statistics.mean(series)
    stdev = statistics.pstdev(series)
    if stdev == 0:
        return []
    return [i for i, value in enumerate(series) if abs((value - mean) / stdev) > z_threshold]
