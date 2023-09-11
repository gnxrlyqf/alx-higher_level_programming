#!/usr/bin/python3
"""defines rebel class that inherits from int."""


class MyInt(int):
    """invert equality and negation operators"""

    def __eq__(self, value):
        """swap == with !="""
        return self.real != value

    def __ne__(self, value):
        """swap != with =="""
        return self.real == value
