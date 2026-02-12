"""VeraGrid integration shim."""

from typing import Any


def run_power_flow(case_path: str) -> dict[str, Any]:
    """Placeholder for VeraGrid run; replace with real integration."""
    return {
        "case": case_path,
        "status": "ok",
        "bus_voltages": [1.00, 0.99, 1.01],
        "line_loading_pct": [62.5, 71.2, 48.3],
    }
