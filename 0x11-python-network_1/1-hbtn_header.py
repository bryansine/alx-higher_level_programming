#!/usr/binpython3
"""A script that: takes in URL,
-then sends a requests to the URL and displays the value
- of thw X-Request-Id variable found in the header responnse.
"""

import sys
import urllib.request

if __name__== "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
