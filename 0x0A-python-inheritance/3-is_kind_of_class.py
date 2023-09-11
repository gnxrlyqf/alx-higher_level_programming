#!/usr/bin/python3
"""checks an inherited class if it's an instance of an object"""


def is_same_class(obj, a_class):
    """check if object is an instance of inherited class

    Args:
        obj (any): object to check
        a_class (type): class to check type of obj
    Returns:
        obj is instance of a_class - True
        otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
