#!/usr/bin/python3
"""define base class"""
import json


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

    def to_json_string(list_dictionaries):
        """return string representation of a list

        Args:
            list_dictionaries (list): list to represent as json dictionary
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
