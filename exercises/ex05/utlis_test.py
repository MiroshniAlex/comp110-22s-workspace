"""List of Tasks."""

__author__ = "730477260"


from exercises.ex05.utils import only_evens, sub, concat


def test_onlyevens_empty() -> None:
    """Empty list only evens."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_onlyevens_one() -> None:
    """Use case one only evens."""
    test_list: list[int] = [2, 5, 6, 11, 10]
    assert only_evens(test_list) == [2, 6, 10]


def test_onlyevens_two() -> None:
    """Use case two only evens."""
    test_list: list[int] = [17, 45, 8, 9, 13]
    assert only_evens(test_list) == [8]


def test_sub_empty() -> None:
    """Empty loss sub."""
    test_list: list[int] = []
    start_idx: int = 0
    end_idx: int = 0
    assert sub(test_list, start_idx, end_idx) == []


def test_sub_one() -> None:
    """Use case one sub."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start_idx: int = 2
    end_idx: int = 7
    assert sub(test_list, start_idx, end_idx) == [3, 4, 5, 6, 7]


def test_sub_two() -> None:
    """Use case two sub."""
    test_list: list[int] = [5, 3, 10, 654, 2, 6, 43]
    start_idx: int = 3
    end_idx: int = 9
    assert sub(test_list, start_idx, end_idx) == [654, 2, 6, 43]


def test_concat_empty() -> None:
    """Empty concat."""
    test_list_one: list[int] = []
    test_list_two: list[int] = []
    assert concat(test_list_one, test_list_two) == []


def test_concat_one() -> None:
    """Use case one concat."""
    test_list_one: list[int] = [1, 2, 3]
    test_list_two: list[int] = [4, 5, 6]
    assert concat(test_list_one, test_list_two) == [1, 2, 3, 4, 5, 6]


def test_concat_two() -> None:
    """Use case two concat."""
    test_list_one: list[int] = [4, 6, -1, 234]
    test_list_two: list[int] = [16, 0, 0, 2, -15, 87]
    assert concat(test_list_one, test_list_two) == [4, 6, -1, 234, 16, 0, 0, 2, -15, 87]