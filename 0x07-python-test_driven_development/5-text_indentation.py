#!/usr/bin/python3
"""
This module contains a function that adds two new lines
after each sentence-ending punctuation.
"""


def text_indentation(text):
    """Prints text, adding two new lines after each '.', '?', or ':' character.

    Args:
        text (str): The string to format.

    Returns:
        None.

    Raises:
        TypeError: If the provided argument is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
