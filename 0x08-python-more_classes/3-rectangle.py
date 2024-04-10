#!/usr/bin/python3

"""This module provides a class for representing rectangles."""


class Rectangle:
    """A class to represent rectangles"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
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
                rectangle_str += '#'
            if y != self.height - 1:
                rectangle_str += '\n'
        return rectangle_str
