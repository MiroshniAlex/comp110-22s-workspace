"""Dictionary related utility functions."""

__author__ = "730477260"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, 'r', encoding='utf8')

    # Prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row the csv line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def certain_attribute_rows(col_data: dict[str, list[str]], header: str, attribute: str) -> dict[str, list[str]]:
    """Takes in col data and returns the rows which match a certian attribute for a certain column."""
    result: dict[str, list[str]] = {}

    # Inintializes correct amount of empty lists to append to.
    # Notice, ignores the header key since their values will all be the same.
    
    for key in col_data:
        if key == header:
            continue
        result[key] = []

    # If the item in header's list matches the attribute name,
    # all of the values for the same row from other columns get appended to their keys.

    for i in range(0, len(col_data[header])):
        if col_data[header][i] == attribute:
            for key in col_data:
                if key == header:
                    continue
                result[key].append(col_data[key][i])
    return result


def column_values(data_rows: list[dict[str, str]], column_name: str) -> list[str]:
    """Takes row data and puts all of the values associated with a certain column name in one column."""
    result: list[str] = []

    for dictionary in data_rows:
        result.append(dictionary[column_name])

    return result


def columnar(data_rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms data from row oriented to column oriented."""
    result: dict[str, list[str]] = {}

    for key in data_rows[0]:
        result[key] = column_values(data_rows, key)
    
    return result


def head(data_column: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Returns the first n rows of a column data."""
    result: dict[str, list[str]] = {}

    if n > len(data_column):
        n = len(data_column)

    for key in data_column:
        n_list: list[str] = []

        for i in range(0, n):
            n_list.append(data_column[key][i])
        
        result[key] = n_list
    
    return result


def select(data_column: dict[str, list[str]], name_list: list[str]) -> dict[str, list[str]]:
    """Returns only a certain selection of columns based on headers."""
    result: dict[str, list[str]] = {}

    for name in name_list:
        result[name] = data_column[name]
    
    return result


def count(value_list: list[str]) -> dict[str, int]:
    """Counts the frequency of values in a column."""
    result: dict[str, int] = {}

    for value in value_list:

        if value in result:
            result[value] += 1

        else:
            result[value] = 1
    
    return result


def organize_keys(data: dict[str, int], order: list[str]) -> dict[str, int]:
    """Organizes the keys of a dictionary in order I choose."""
    result: dict[str, int] = {}
    for item in order:
        result[item] = 0
    for key in data:
        result[key] = data[key]
    return result