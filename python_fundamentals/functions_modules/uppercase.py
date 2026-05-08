#!/usr/bin/env python3

def uppercase(str):
    """Prints str in uppercase followed by a new line"""
    string_to_print = ""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            string_to_print += chr(ord(c) - 32)
        else:
            string_to_print += c
    print("{}".format(string_to_print))
