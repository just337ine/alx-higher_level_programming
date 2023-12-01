#!/usr/bin/python3
"""
usage:
    ./1-hbtn_header.py url
"""

import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    result = response.headers.get('X-Request-Id')

if __name__ == "__main__":
    print(result)
