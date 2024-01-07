#!/usr/bin/python3
from urllib import request, error
import sys
if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as page:
            data = page.read()
            print(data.decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))