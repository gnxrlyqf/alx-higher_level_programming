#!/usr/bin/python3
"""fetches data from url"""

from urllib import request
with request.urlopen("https://alx-intranet.hbtn.io/status") as page:
    data = page.read()
    print("Body response:")
    print("\t- type: ", type(data))
    print("\t- content: ", data)
    print("\t- utf8 content: ", data.decode("utf-8"))
