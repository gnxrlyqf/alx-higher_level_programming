#!/usr/bin/python3
"""prints http error code"""
from urllib import request, error
from sys import argv
if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as page:
            data = page.read()
            print(data.decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
