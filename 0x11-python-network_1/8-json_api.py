#!/usr/bin/python3
"""sends a post request and retrieves json response"""
from sys import argv
from requests import post, get
if __name__ == "__main__":
    if len(argv) == 1:
        v = ""
    else:
        v = argv[1]
    data = {"q": v}
    with post("http://0.0.0.0:5000/search_user", data=data) as page:
        try:
            out = page.json()
            if not out:
                print("No result")
            else:
                print("[{}] {}".format(out.get("id"), out.get("name")))
        except ValueError:
            print("Not a valid JSON")
