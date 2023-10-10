#!/usr/bin/python3
"""json to object function"""
import json


def from_json_string(my_str):
    """return json as an object"""
    return json.loads(my_str)