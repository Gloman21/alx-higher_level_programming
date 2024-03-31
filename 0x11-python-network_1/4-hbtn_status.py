#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""

import requests
url = 'https://alx-intranet.hbtn.io/status'
result = requests.get(url, timeout=5)
print("Body response:")
print(f"\t- type: {type(result.text)}")
print(f"\t- content: {result.text}")
