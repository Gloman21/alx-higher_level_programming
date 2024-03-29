#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen("https://intranet.hbtn.io/status") as response:
        info = response.read()
        if info:
            print("Body response:")
            print("\t- type: {}".format(type(info)))
            print("\t- content: {}".format(info))
            print("\t- utf8 content: {}".format(info.decode("utf-8")))
        else:
            print("Response is empty")
