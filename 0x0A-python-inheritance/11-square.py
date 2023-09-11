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

    def area(self):
        """area of square"""
        return self.__size * self.__size

    def __str__(self):
        """represent square as str"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
