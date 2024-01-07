#!/usr/bin/python3
"""prints http error code"""
from urllib import request, error
import sys
if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as page:
            data = page.read()
            print(data.decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
