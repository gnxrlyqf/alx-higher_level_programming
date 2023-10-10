#!/usr/bin/python3
"""add argv to json file"""
import sys

if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    try:
        arr = load("add_item.json")
    except FileNotFoundError:
        arr = []
    arr.extend(sys.argv[1:])
    save_to_json_file(arr, "add_item.json")
