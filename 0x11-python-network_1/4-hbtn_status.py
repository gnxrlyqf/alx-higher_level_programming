#!/usr/bin/python3
"""fetches webpage using requests"""
import requests
if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as page:
        content = page.content.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))