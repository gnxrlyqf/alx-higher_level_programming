#!/usr/bin/python3
"""file writing function"""


def append_write(filename="", text=""):
    """append to a file

    Args:
        filename (str): file to append to
        text (str): text to append
    Returns:
        number of bytes written
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
