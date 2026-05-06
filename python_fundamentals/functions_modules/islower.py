#!/usr/bin/env python3

def islower(c):
    """Return True if c is a lowercase letter and False otherwise"""
    if ord(c) >= 97 and ord(c) <= 172:
        return True
    return False
