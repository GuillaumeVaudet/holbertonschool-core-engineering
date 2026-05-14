#!/usr/bin/env python3

def safe_print_integer(value: int):
    """Display an integer followed by a new line"""
    if isinstance(value, bool):
        return False
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
