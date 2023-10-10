#!/usr/bin/python3
"""class checking function"""


def is_same_class(obj, a_class):
    """check of obj is exactly an instance of a_class

    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        obj is exactly an instance of a class - True
        otherwise - False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
