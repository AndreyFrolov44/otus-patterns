import math

eps = 1e-5


def solve(a: float, b: float, c: float) -> list[float]:
    if (
        math.isinf(a)
        or math.isinf(b)
        or math.isinf(c)
        or math.isnan(a)
        or math.isnan(b)
        or math.isnan(c)
    ):
        raise ValueError("a, b and c cannot be infinite or nan")
    if abs(a) < eps:
        raise ValueError("a cannot be zero")

    d = b**2 - 4 * a * c

    if d < 0:
        return []

    if d < eps and d >= 0:
        return [-b / (2 * a)]

    x1 = (-b + d**0.5) / (2 * a)
    x2 = (-b - d**0.5) / (2 * a)

    return [x1, x2]
