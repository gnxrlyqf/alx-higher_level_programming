#!/usr/bin/python3
"""functin that adds attributes"""


def add_attribute(obj, att, value):
    """add new attribute

    Args:
        obj (any): object to process
        att (str): name of attribute
        value (any): attribute value
    Raises:
        TypeError: attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
