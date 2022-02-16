"""Example of writing a test subject."""


def sum(xs: list[float]) -> float:
    """Compute the sum opf a list."""
    total: float = 0.0
    for i in range(0, len(xs)):
        total += xs[i]
    return total
