"""OPF dispatch recommendation helpers."""


def create_dispatch_hint(objective_value: float) -> str:
    return f"Apply OPF dispatch plan (objective={objective_value:.2f})"
