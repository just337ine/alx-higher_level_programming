#!/usr/bin/python3
for alpha in reversed(range(ord("a"), ord("z") + 1)):
    if alpha % 2 != 0:
        alpha = alpha - 32
    print("{:c}".format(alpha), end="")
