"""Checking a List of Tasks."""

__author__ = "730477260"


def only_evens(nums: list[int]) -> list[int]:
    """Only evens in a list."""
    evens: list[int] = []
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            evens.append(nums[i])
    return evens


def sub(nums: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Takes limited range of list."""
    sub_list: list[int] = []
    if end_idx < 0 or start_idx > len(nums) - 1:
        return sub_list
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(nums):
        end_idx = len(nums)
    for i in range(start_idx, end_idx):
        sub_list.append(nums[i])
    return sub_list


def concat(first_list: list[int], second_list: list[int]):
    """Appends one list to the other."""
    for i in range(0, len(second_list)):
        first_list.append(second_list[i])
    return first_list