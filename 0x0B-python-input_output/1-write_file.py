#!/usr/bin/python3
"""a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    with open(filename, mode='w') as f:
        return f.write(text)
