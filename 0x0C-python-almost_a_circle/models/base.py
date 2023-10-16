#!/usr/bin/python3
"""define base class"""


class Base:
    """base class

    Private Classes Attributes:
        __nb_objects (int): instance count
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
