"""Network probability helpers."""

def at_least_one_success(single_success: float, copies: int) -> float:
    """Independent-copy success probability; do not use for common incidents."""
    return 1.0 - (1.0 - single_success) ** copies
