from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_15_and_24() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_24() -> None:
    assert get_human_age(24, 24) == [2, 2]
