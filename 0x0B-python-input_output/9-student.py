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

    def to_json(self):
        """represent student as dictionary"""
        return self.__dict__
