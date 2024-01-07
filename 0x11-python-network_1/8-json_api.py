#!/usr/bin/python3
"""sends a post request and retrieves json response"""
from sys import argv
from requests import post
if __name__ == "__main__":
    data = {"q": argv[1]}
    with post("http://0.0.0.0:5000/search_user", data=data) as page:
        try:
            out = page.json()
            if not out:
                print("No result")
            else:
                print("[{}] {}".format(page.get("id"), page.get("name")))
        except ValueError:
            print("Not a valid JSON")
