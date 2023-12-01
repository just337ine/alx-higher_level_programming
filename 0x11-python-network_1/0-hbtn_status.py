#!/usr/bin/python3
"""
usage:
    python3 0-htbn_ataus.py
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    html = response.read()

if __name__ == "__main__":
    print("Body response:\n\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
