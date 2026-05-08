#!/usr/bin/env python3

from add_0 import add


def addition():
    """use the function add to resolve an addition"""
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))


if __name__ == "__main__":
    addition()
