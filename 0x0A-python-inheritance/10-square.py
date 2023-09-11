#!/usr/bin/python3
"""defines square subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent square"""

    def __init__(self, size):
        """construct new square

        Args:
            size (int): square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
