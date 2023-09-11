#!/usr/bin/python3
"""checks an inherited class"""


def inherits_from(obj, a_class):
    """checks if object is an inherited instance of class

    Args:
        obj (any): object to check
        a_class (type): class to check the type of obj
    Returns:
        if obj is an inherited instance of a_class - Tru.
        otherwise - False.
    """
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
