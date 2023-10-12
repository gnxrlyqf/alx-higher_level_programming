#!/usr/bin/python3
"""MyInt class inheriting from int"""


class MyInt(int):
    """invert == and != operators"""

    def __eq__(self, value):
        """replace == with !="""
        return self.real != value

    def __ne__(self, value):
        """replace != with =="""
        return self.real == value
