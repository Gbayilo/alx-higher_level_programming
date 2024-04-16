#!/usr/bin/python3
"""Module conatinsn a function"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n
    """

    if n <= 0:
        return []

    p_triangle = [[1]]

    for i in range(1, n):
        row = [1]
        previous_row = p_triangle[i - 1]
        for j in range(1, i):
            row.append(previous_row[j - 1] + previous_row[j])
        row.append(1)

        p_triangle.append(row)

    return p_triangle
