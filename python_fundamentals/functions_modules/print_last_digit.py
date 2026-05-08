#!/usr/bin/env python3

def print_last_digit(number):
    """Print the last digit of number"""

    last_digit = abs(number) % 10
    print("{}".format(last_digit))

    return last_digit
