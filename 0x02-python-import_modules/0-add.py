#!/usr/bin/python3

if __name__ == "__main__":
    a = 1
    b = 2

    from add_0 import add

    result = add(a, b)
    print('{:d} + {:d} = {:d}'.format(a, b, result))
