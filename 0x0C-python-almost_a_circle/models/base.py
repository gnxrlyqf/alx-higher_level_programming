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
        """return string representation of a list"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
