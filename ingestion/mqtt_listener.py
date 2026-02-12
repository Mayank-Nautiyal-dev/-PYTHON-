"""MQTT ingestion stub for GridGuard AI."""

from datetime import datetime
from typing import Any


def normalize_payload(payload: dict[str, Any]) -> dict[str, Any]:
    """Normalize raw telemetry payload into canonical schema."""
    return {
        "timestamp": payload.get("timestamp", datetime.utcnow().isoformat()),
        "load_mw": float(payload.get("load_mw", 0.0)),
        "voltage_kv": float(payload.get("voltage_kv", 0.0)),
        "temperature_c": float(payload.get("temperature_c", 0.0)),
        "humidity": float(payload.get("humidity", 0.0)),
    }
