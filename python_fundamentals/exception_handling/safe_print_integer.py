#!/usr/bin/env python3

def safe_print_integer(value: int):
    """Display an integer followed by a new line"""
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    print_bool = safe_print_integer(True)
    ok = safe_print_integer(3)
    print_float = safe_print_integer(3.5)
    nok = safe_print_integer('z')

    print(print_bool)
    print(ok)
    print(print_float)
    print(nok)
