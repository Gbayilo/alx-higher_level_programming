#!/usr/bin/python3
"""Read text file and prints to stdout"""


def read_file(filename=""):
    """Reads a text file with UT8 encoding and prints to stdout."""

    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()
        print(file_content, end='')
