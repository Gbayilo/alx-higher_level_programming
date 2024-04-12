#!/usr/bin/python3
"""
A module that provides a function for dividing all
elements of a matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        divisor (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with all elements divided by the divisor.

    Raises:
        TypeError: If the divisor is not a number,
        or if the matrix is not a list of lists of integers/floats,
        or if any row of the matrix does not have the same size.
        ZeroDivisionError: If the divisor is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [list(map(lambda num: round(num / div, 2), row)) for row in matrix]
