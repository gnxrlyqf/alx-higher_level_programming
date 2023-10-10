#!/usr/bin/python3
"""json reading function"""
import json


def load_from_json_file(filename):
    """read json as python object"""
    with open(filename) as f:
        return json.load(f)
