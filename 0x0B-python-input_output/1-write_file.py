#!/usr/bin/python3
"""file writing function"""


def write_file(filename="", text=""):
    """write to a file

    Args:
        filename (str): file to write to
        text (str): text to write
    Returns:
        number of bytes written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
