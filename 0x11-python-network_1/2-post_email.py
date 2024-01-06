#!/usr/bin/python3
"""send a post request to a url"""
from urllib import parse, request
import sys
if __name__ == "__main__":
    data = {"email": sys.argv[2]}
    data = parse.urlencode(data)
    data = data.encode("ascii")
    req = request.Request(sys.argv[1], data=data)
    with request.urlopen(req) as response:
        out = response.read().decode("utf-8")
        print(out)
