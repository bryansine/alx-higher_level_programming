#!/usr/bin/python3
"""A Bash script that: takes in URL
-sends a POST request to the passed URL
- then takes emailas parameter
-finally displays the body of the response
"""

import sys
import urllib.parse
import urllib.request


if __name__== "__main_":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
