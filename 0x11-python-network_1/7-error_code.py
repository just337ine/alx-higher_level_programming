#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    url = requests.get(argv[1])
    if url.status_code >= 400:
        print("Error code: {}".format(url.status_code))
    else:
        print(url.text)
