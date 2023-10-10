#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer parameter

        Args:
            name (str): parameter name
            value (int): value to validate
        Raises:
            TypeError: value is not int
            ValueError: value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
