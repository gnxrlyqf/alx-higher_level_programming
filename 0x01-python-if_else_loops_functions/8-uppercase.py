#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ch = chr(ord(c) - 32) if (ord(c) >= 97 and ord(c) <= 124) else c
        print("{}".format(ch), end="")
    print()
