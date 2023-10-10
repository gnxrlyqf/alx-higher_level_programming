#!/usr/bin/python3
"""write json file"""
import json


def save_to_json_file(my_obj, filename):
    """write object to file as json"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
