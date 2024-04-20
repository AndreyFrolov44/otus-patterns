import pytest

from home_work_1.main import solve


@pytest.mark.parametrize(
    ("a", "b", "c", "expected"),
    [
        (1, 0, 1, []),
        (1, 0, -1, [1.0, -1.0]),
        (1, 2, 1, [-1.0]),
    ],
)
def test_solve(a, b, c, expected):
    assert solve(a, b, c) == expected


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        ((float("inf"), 1, 1)),
        ((1, float("inf"), 1)),
        ((1, 1, float("inf"))),
        ((float("-inf"), 1, 1)),
        ((1, float("-inf"), 1)),
        ((1, 1, float("-inf"))),
        ((float("nan"), 1, 1)),
        ((1, float("nan"), 1)),
        ((1, 1, float("nan"))),
        (0, 1, 1),
    ],
)
def test_validate_a(a, b, c):
    with pytest.raises(ValueError):
        solve(a, b, c)
