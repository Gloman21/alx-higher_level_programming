#!/usr/bin/python3
""" Script that takes URL, sends requests and displays value of X-Request-Id"""

    import sys
    import urllib.request

    if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader["X-Request-Id"])
