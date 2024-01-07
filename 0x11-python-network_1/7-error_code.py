#!/usr/bin/python3
"""request a url and print status code"""
from sys import argv
from requests import get, HTTPError
if __name__ == "__main__":
    with get(argv[1]) as page:
        if page.status_code >= 400:
            print("Error code: {}".format(page.status_code))
        else:
            print(page.content.decode("utf-8"))
