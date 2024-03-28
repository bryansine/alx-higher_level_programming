#!/usr/bin/python3
"""A bash script that: takes in a letter
-then sends POST request to http://0.0.0.0.5000/search_user
with the letter as a parameter.
"""

import sys
import requests


if __name __ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0.5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name:)))
    except valueError:print("Not a valid JSON")