#!/usr/bin/python3
"""class checking function"""


def is_kind_of_class(obj, a_class):
    """check of obj is instance of a_class

    Args:
        obj (any): object to check
        a_class (type): class to check
    Returns:
        obj is an instance of a class - True
        otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
