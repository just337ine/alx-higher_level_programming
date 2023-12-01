#!/usr/bin/python3
"""
usage:
    ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv

    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    url = request.Request(argv[1], data)
    with request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
