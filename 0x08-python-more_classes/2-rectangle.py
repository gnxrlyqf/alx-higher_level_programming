#!/usr/bin/python3
"""defines class"""


class Rectangle:
    """represent triangle"""

    @property
    def width(self):
        """width getter/setter"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter/setter"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """object constructor

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height

    def area(self):
        """returns rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """returns rectangle perimeter"""
        zero = 1
        if self.width == 0 or self.height == 0:
            zero = 0
        return (self.height * 2 + self.width * 2) // zero
