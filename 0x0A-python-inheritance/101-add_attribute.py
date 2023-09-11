#!/usr/bin/python3
"""defines function that adds attributes"""


def add_attribute(obj, att, value):
    """add new attribute to object

    Args:
        obj (any): object to change
        att (str): attribute to add
        value (any): attribute value
    Raises:
        TypeError: attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
