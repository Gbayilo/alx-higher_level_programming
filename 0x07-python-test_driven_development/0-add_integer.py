#!/usr/bin/python3
""" Define an integer addition function. """


def add_integer(a, b=98):
    """ Add two integers

    Args:
      a (int): First Number.
      b (int) (optional): Second Number.

    Return: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
