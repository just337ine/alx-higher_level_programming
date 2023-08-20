#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    result = 0
    operator_error = False

    match operator:
        case '+':
            result = add(a, b)
        case '-':
            result = sub(a, b)
        case '*':
            result = mul(a, b)
        case '/':
            result = div(a, b)
        case _:
            operator_error = True

    if operator_error:
        print("Unknow operator. Available operators: +, -, *,and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}". format(a, operator, b, result))
