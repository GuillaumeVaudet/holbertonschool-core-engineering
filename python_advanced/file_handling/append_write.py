#!/usr/bin/env python3
"""Python module to append into a text file"""


def append_write(filename="", text=""):
    """Function that appends a string into file and
    return number of char added"""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
