#!/usr/bin/python3
"""Writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file using UTF8 encoding
    and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
