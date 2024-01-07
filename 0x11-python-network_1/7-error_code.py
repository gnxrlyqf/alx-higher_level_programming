#!/usr/bin/python3
"""request a url and print status code"""
from sys import argv
from requests import get, HTTPError
if __name__ == "__main__":
    try:
        with get(argv[1]) as page:
            print(page.content.decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
