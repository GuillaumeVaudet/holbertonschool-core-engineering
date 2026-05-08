#!/usr/bin/env python3

def uppercase(str):
    """Prints str in uppercase followed by a new line"""
    for c in str:
        if ord(c) >= ord('A') and ord(c) <= ord('Z'):
            print(c, end="")
        else:
            print("{}".format(chr(ord(c) - 32)), end="")
    print()
