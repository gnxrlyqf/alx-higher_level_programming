#!/usr/bin/python3
def upper(str):
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 124):
            print("{}".format(chr(ord(c) - 32)))
        else:
            print(c)