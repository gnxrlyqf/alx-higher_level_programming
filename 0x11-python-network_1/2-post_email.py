#!/usr/bin/python3
"""send a post request to a url"""
from urllib import parse, request
import sys
if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    string = parse.urlencode(email)
    req = request.urlopen(sys.argv[1], data=string)
    with request.urlopen(request) as response:
        out = response.read().decode("utf-8")
        print(out)
