#!/usr/bin/python3
"""file reading function"""


def read_file(filename=""):
    """read and print a file"""
    with open(filename, encoding = "utf-8") as file:
        print(file.readlines())
