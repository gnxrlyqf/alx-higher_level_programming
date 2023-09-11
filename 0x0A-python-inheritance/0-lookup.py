#!/usr/bin/python3
"""lookup available attributes for an object"""


def lookup(obj):
    """list an object's available attributes"""
    return (dir(obj))
