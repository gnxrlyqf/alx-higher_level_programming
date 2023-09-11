#!/usr/bin/python3
"""defines class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent rectangle"""

    def __init__(self, width, height):
        """construct new rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """represent rectangle as str"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
