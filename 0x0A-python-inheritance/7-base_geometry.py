#!/usr/bin/python3
"""defines class BaseGeometry"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """no implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate parameter as integer

        Args:
            name (str): name of the parameter
            value (int): parameter to validate
        Raises:
            TypeError: value is not int
            ValueError: value is negative
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
