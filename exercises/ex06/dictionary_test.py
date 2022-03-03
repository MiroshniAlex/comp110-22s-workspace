"""Testing my dicitonaries."""

__author__ = "730477260"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_empty() -> None:
    """Tests invert of empty dicitonary."""
    assert invert({}) == {}


def test_invert_key_error() -> None:
    """Tests whether the KeyError message appears."""
    with pytest.raises(KeyError):
        dictionary: dict[str, str] = {'a': '1', 'b': '1'}
        invert(dictionary)


def test_invert_use_case_one() -> None:
    """Invert use case one."""
    dictionary: dict[str, str] = {'a': '1', 'b': '2', 'c': '3'}
    assert invert(dictionary) == {'1': 'a', '2': 'b', '3': 'c'}


def test_invert_use_case_two() -> None:
    """Invert use case two."""
    dictionary: dict[str, str] = {'abc': '123', '789': 'xyz', 'sam': 'short'}
    assert invert(dictionary) == {'123': 'abc', 'xyz': '789', 'short': 'sam'}


def test_favorite_color_empty() -> None:
    """Tests favorite_color empty case."""
    assert favorite_color({}) == ""


def test_favorite_color_use_case_one() -> None:
    """Tests one use case of favorite_color."""
    name_color: dict[str, str] = {
        'Sally': 'pink',
        'John': 'green',
        'Sam': 'green'
    }
    assert favorite_color(name_color) == 'green'


def test_favorite_color_use_case_two() -> None:
    """Tests second use case of favorite_color."""
    name_color: dict[str, str] = {
        'Sally': 'pink',
        'John': 'green',
        'Sam': 'green',
        'Josh': 'pink'
    }
    assert favorite_color(name_color) == 'pink'


def test_count_empty() -> None:
    """Tests empty count edge case."""
    assert count([]) == {}


def test_count_use_case_one() -> None:
    """Tests use case one count."""
    my_list: list[str] = ['a', 'a', 'b', 'c', 'a', 'c']
    assert count(my_list) == {'a': 3, 'b': 1, 'c': 2}


def test_count_use_case_two() -> None:
    """Tests use case two count."""
    my_list: list[str] = ['j', 'h', 'k', 'd', 'h', 'j']
    assert count(my_list) == {'h': 2, 'j': 2, 'd': 1, 'k': 1}