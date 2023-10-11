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
        self.width = width
        self.integer_validator("height", height)
        self.height = height
