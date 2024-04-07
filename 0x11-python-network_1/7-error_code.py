#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    URL = sys.argv[1]
    result = requests.get(URL, timeout=5)
    if result.status_code >= 400:
        print(f"Error code: {RESULT.status_code}")
    else:
        print(result.text)
