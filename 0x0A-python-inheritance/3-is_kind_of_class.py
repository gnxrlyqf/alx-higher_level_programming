#!/usr/bin/python3
"""checks an inherited class"""


def is_same_class(obj, a_class):
    """check if object is an instance of class

    Args:
        obj (any): object to check
        a_class (type): class to check type of obj
    Returns:
    obj is an instance of a_class - True
        otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
