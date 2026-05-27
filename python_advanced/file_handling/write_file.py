#!/usr/bin/env python3
"""Python module to write into a text file"""


def write_file(filename="", text=""):
    """Function that writes into file and return number of char written"""
    with open(filename, "w", encoding="utf-8") as file:
        nb_of_words = file.write(text)
    return nb_of_words
