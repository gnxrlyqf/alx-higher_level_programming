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
        if self.width == 0 or self.height == 0:
            return 0
        return self.height * 2 + self.width * 2

    def __str__(self):
        """prints rectangles using #"""
        if self.width == 0 or self.height == 0:
            return ("")

        arr = []
        for i in range(self.height):
            for j in range(self.width):
                arr.append('#')
            if i != self.height - 1:
                arr.append("\n")
        return ("".join(arr))
