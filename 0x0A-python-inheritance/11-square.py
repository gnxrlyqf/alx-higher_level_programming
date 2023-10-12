#!/usr/bin/python3
"""defines square class inheriting from rectangle"""
parent = __import__('9-rectangle').Rectangle


class Square(parent):
    """represent square"""

    def __init__(self, size):
        """square constructor

        Args:
            size (int): square size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

	def __str__(self):
        """represent square as string"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
