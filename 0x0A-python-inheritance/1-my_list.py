#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """prints sorted list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))