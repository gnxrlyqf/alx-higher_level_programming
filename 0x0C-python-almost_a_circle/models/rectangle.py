#!/usr/bin/python3
"""define new rectangle class"""
from models.base import Base


class Rectangle(Base):
    """represent rectangle"""
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

    def __init__(self, width, height, x=0, y=0, id=None):
        """rectangle constructor

        Args:
            width (int): rectangle width
            height (int): rectangle height
            x (int): rectangle x offset
            y (int): rectangle y offset
            id (int): rectangle id
        Raises:
            TypeError: width or height are not ints
            ValueError: negative or null width or height
            TypeError: x or y offstes are not ints
            ValueError: negative or null x and y offsets
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """return rectangle area"""
        return self.width * self.height

    def display(self):
        """print rectangle in #'s"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(end=" ")
            for k in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """represent rectangle as string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def to_dictionary(self):
        """represent rectangle as dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
