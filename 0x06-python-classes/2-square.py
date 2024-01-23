#!/usr/bin/python3
"""A class Square with size"""


class Square:
    """class - square"""

    def __init__(self, size: int = 0):
        """
        Initialize class square

        Args: size - size of the square

        Raises:
            TypeError: when the size received is not an integer
            ValueError: when the size if not a positive integer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
