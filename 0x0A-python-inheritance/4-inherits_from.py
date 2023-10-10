#!/usr/bin/python3
"""inherited class function"""


def inherits_from(obj, a_class):
    """check if obj inherits from a_class

    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        if object inherits from class - True
        Otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
