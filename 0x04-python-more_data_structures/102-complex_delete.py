#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keylist = list(a_dictionary.keys())
    for val in keylist:
        if val == value:
            del a_dictionary[val]
    return a_dictionary
