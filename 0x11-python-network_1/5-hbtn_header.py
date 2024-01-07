#!/usr/bin/python3
"""fetches  header variable"""
import requests
from sys import argv
if __name__ == "__main__":
    with requests.get(argv[1]) as page:
        print(page.headers["X-Request-Id"])
