#!/usr/bin/python3
"""defines class inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle"""

    def __init__(self, width, height):
        """construct new rectangle

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
