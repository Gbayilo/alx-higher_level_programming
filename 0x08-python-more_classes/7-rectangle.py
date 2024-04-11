#!/usr/bin/python3
"""This module provides a class for representing rectangles."""


class Rectangle:
    """A class to represent rectangles"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance\
        with the specified width and height.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero

        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for private instance width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        rectangle_str = ''
        if self.__height == 0 or self.__width == 0:
            return rectangle_str
        for y in range(self.height):
            for x in range(self.width):
                rectangle_str += str(self.print_symbol)
            if y != self.height - 1:
                rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
