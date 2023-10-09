#!/usr/bin/python3
"""attribute lookup function"""


def lookup(obj):
    """return a list of object attributes available"""
    return (dir(obj))
