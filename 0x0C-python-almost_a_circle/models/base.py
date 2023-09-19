#!/usr/bin/python3


class Base:
    """base model for all models inheriting from it

    Private Class Attributes:
        __nb_object (int): number of objects instantiated
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
