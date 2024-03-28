#!/usr/bin/python3
""""A scrupt that: takes in a URL,
-then sends a request to the URL
- displays the body of the response.
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPerror as er:
        print('Error code:', er.code)
