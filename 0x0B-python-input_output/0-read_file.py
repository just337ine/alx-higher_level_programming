#!/usr/bin/python3
def read_file(filename=""):
    """A function that reads a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
            f.closed
