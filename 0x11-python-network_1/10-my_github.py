#!/usr/bin/python3
"""displays an id using github auth"""
from sys import argv
from requests import auth, get


if __name__ == "__main__":
    auth = auth.HTTPBasicAuth(argv[1], argv[2])
    with get("https://api.github.com/user", auth=auth) as page:
        print(page.json().get("id"))
