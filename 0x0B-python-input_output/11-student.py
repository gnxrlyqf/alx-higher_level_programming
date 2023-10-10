#!/usr/bin/python3
"""studnet class"""


class Student:
    """student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): studnet's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """represent student as dictionary
            Args:
        attrs (list): (Optional) The attributes to represent
        """
        if (type(attrs) == list and all(type(e) == str for e in attrs)):
            new_dictionary = {}
            for k in attrs:
                if hasattr(self, k):
                    new_dictionary[k] = getattr(self, k)
            return new_dictionary
        return self.__dict__

    def reload_from_json(self, json):
        """replace student attributes

        Args:
            json (dict): dictionary elements to replace attributes with
        """
        for key, value in json.items():
            setattr(self, key, value)
