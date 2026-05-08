#!/usr/bin/env python3

from add_0 import add


def addition():
    """Resolve addition of 1 and 2 using the add function from add_0.py"""
    a = 1
    b = 2
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))


if __name__ == "__main__":
    addition()