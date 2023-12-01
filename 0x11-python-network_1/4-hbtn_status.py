#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests
    url = requests.get('https://alx-intranet.hbtn.io/status')
    response = url.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
