#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    for i in range(len(str)):
        string += str[i] if i != n else ""
    return string
