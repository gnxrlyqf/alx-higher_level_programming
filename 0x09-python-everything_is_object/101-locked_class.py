#!/usr/bin/python3
"""defines locked class"""

class LockedClass:
    """
    only let use create attributes for first name
    """
    __slots__ = ["first_name"]
