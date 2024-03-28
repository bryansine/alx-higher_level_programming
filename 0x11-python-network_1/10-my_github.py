#!/usr/bin/python3
"""A bash script that:
- takes your Github credentials (username and password)
- then uses Github API to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
