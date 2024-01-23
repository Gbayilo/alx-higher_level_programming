#!/usr/bin/python3
"""Defines a square"""


class Square:
    """class - Square """

    def __init__(self, size=0):
        """Initializes sqaure class"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)
