"""Its a dictionary bro."""

__author__ = "730477260"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Swaps the keys and values of a dictionary."""
    inv_dict: dict[str, str] = {}
    for key in dictionary:
        inv_dict[dictionary[key]] = key
    if len(inv_dict) != len(dictionary):
        raise KeyError("KeyError")
    return inv_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most used value. If tie, returns the first one seen."""
    counter: dict[str, int] = {}
    most_frequent: str = ""

    # A new dicitonary, counter, keeps track of how many of each value is in the original dictionary.

    for name in dictionary:
        if dictionary[name] in counter:
            counter[dictionary[name]] += 1
        else:
            counter[dictionary[name]] = 1
    
    # Goes through the counter dict to find the highest value.

    for color in counter:
        if most_frequent == "":
            most_frequent = color
        elif counter[color] > counter[most_frequent]:
            most_frequent = color
    
    return most_frequent


def count(my_list: list[str]) -> dict[str, int]:
    """Counts the occurances of a str in a list and returns dict[str, occurances]."""
    counter: dict[str, int] = {}
    for n in my_list:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1
    return counter