#!/usr/bin/python3
"""
This module, '4-print_square', provides a single function, print_square(size),
which is designed to print a square made of '#'
characters with a specified side length.
"""


def print_square(size):
    """Draws a square using the '#' character with sides of length 'size'."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
