#!/usr/bin/env python3
"""Python module to write file"""


def read_file(filename=""):
    """Function that reads an utf-8 text file"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
