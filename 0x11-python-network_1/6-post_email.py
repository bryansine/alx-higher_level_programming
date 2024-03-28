#!/usr/bin/python3
"""A script that:takes in a URL and an email adrres
- then sends a POSt request to the passed URL with the
- email as a parameter displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[2]}
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)
