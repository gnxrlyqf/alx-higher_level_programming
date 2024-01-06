#!/usr/bin/python3
"""displays header value of a webpage"""
from urllib import request
import sys
if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as page:
        header = page.getheader("X-Request-Id")
        print(header)
