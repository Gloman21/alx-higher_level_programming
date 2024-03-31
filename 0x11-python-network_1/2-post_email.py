#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request, and displays the body of the response"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    email =sys.argv[2]
    DATA = urllib.parse.urlencode({"email": email}).encode('ascii')
    request = urllib.request.Request(URL, DATA, method="POST")
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
