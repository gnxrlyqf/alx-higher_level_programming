#!/usr/bin/python3
"""fetches data from url"""
from urllib import request
if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as page:
        data = page.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))
