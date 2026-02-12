"""Rule-based recommendation engine."""


def recommend_actions(overload: float) -> list[str]:
    if overload > 0.9:
        return [
            "Activate backup transformer",
            "Shift industrial load",
            "Start demand response program",
        ]
    return ["No critical action required"]
