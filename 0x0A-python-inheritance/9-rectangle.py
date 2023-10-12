#!/usr/bin/python3
"""rectangle class inheriting from basegeometry"""
parent = __import__('7-base_geometry').BaseGeometry


class Rectangle(parent):
    """represent rectangle"""

    def __init__(self, width, height):
        """rectangle constructor

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
