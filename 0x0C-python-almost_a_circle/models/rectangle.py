#!/usr/bin/python3
"""rectangle class inheriting from base"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance constructor
        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): rectangle x position
            y (int): rectangle y position
            id (int): rectangle id
        Raises:
            TypeError: if width, height, x or y is int
            ValueError: if width or height is <= 0
            ValueError: if x or y is < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """setter/getter for rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """setter/getter for rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """setter/getter for rectangle x position"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """setter/getter for rectangle y position"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(end=" ")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """return Rectangle str representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update rectangle

        Args:
            *args (ints): new arbitrary values
                - 1st argument represents id
                - 2nd argument represents width
                - 3rd argument represents height
                - 4th argument represents x
                - 5th argument represents y
            **kwargs (dict): dictionary values
        """
        if args and len(args) != 0:
            if args[0] is None:
                self.__init__(self.width, self.height, self.x, self.y)
            else:
                self.id = args[0]
            if 1 < len(args):
                self.width = args[1]
            if 2 < len(args):
                self.height = args[2]
            if 3 < len(args):
                self.x = args[3]
            if 4 < len(args):
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """represent square as dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
