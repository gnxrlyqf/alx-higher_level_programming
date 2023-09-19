#!/usr/bin/python3
"""define new square class"""
from models.base import Base


class Square(Base):
    """represent rsquare"""
    def update(self, *args, **kwargs):
        """update square

        Args:
            *args (ints): new arbitrary values
                - 1st argument represents id
                - 2nd argument represents size
                - 3rd argument represents x
                - 4th argument represents y
            **kwargs (dict): dictionary values
        """
        if args and len(args) != 0:
            if args[0] is None:
                self.__init__(self.size, self.x, self.y)
            else:
                self.id = args[0]
            if 1 < len(args):
                self.size = args[1]
            if 2 < len(args):
                self.x = args[2]
            if 3 < len(args):
                self.y = args[3]

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    @property
    def size(self):
        """setter/getter for square size"""
        return self.width

    @size.setter
    def width(self, value):
        self.width = value
        self.height = value

    def __init__(self, size, x=0, y=0, id=None):
        """square constructor

        Args:
            size (int): square size
            x (int): rectangle x offset
            y (int): rectangle y offset
            id (int): rectangle id
        Raises:
            TypeError: size is not int
            ValueError: negative or null size
            TypeError: x or y offstes are not ints
            ValueError: negative or null x and y offsets
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """represent square as string"""
        return "[Rectangle] ({}) {}/{} - {}".format(self.id,
                                                    self.x, self.y, self.width)

    def to_dictionary(self):
        """represent square as dictionary"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
