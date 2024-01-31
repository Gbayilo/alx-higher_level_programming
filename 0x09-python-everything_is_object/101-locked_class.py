#!/usr/bin/python3
"""
Defines class Lockedclass with no class or object attribute
"""


class LockedClass():
    """
    prevents user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    """

    __slots__ = "first_name"
