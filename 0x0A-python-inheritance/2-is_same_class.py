#!/usr/bin/python3
"""checks a class"""


def is_same_class(obj, a_class):
    """check if object is exactly an instance of class.

    Args:
        obj (any): object to check
        a_class (type): class to check type of obj
    Returns:
        obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, class):
        return True
    return False