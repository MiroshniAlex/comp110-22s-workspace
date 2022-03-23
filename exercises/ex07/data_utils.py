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


def concat(data_column_one: dict[str, list[str]], data_column_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column oriented data sets."""
    result: dict[str, list[str]] = {}

    for key in data_column_one:
        result[key] = data_column_one[key]

    for key in data_column_two:

        if key in result:

            for n in range(len(data_column_two[key])):
                result[key].append(data_column_two[key][n])

        else:
            result[key] = data_column_two[key]
    
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