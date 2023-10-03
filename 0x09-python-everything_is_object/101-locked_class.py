#!/usr/bin/python3
"""defines locked"""


class LockedClass:
    """
	prevents instantiation of new instances by user

    Attributes:
        first_name (str): first name
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """construct for new class instance"""

        self.first_name = "first_name"