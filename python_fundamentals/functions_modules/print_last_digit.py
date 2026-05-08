#!/usr/bin/env python3

def print_last_digit(number):
    """Print the last digit of number"""

    if number < 0:
        number = number * -1
    
    last_digit = number % 10
    print("{}".format(last_digit))
    return last_digit
