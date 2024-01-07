#!/usr/bin/python3
"""sends a post request to a url"""
from sys import argv
from requests import post
if __name__ == "__main__":
    data = {"email": argv[2]}
    with post(argv[1], data=data) as reponse:
        print(reponse)
