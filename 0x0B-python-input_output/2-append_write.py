#!/usr/bin/python3
"""Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file.

         Args:
            filename (str): The name of the file to append to.
            text (str): The string to append to the file.
    """

    with open(filename, 'a') as file:
        return file.write(text)
