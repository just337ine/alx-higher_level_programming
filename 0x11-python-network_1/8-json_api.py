#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    url = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        url_dict = url.json()
        id = url_dict.get('id')
        name = url_dict.get('name')
        if len(url_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(url_dict.get('id'), url_dict.get('name')))
    except:
        print("Not a valid JSON")
