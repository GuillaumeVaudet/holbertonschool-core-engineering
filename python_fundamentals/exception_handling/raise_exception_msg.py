#!/usr/bin/env

def raise_exception_msg(message=""):
    try:
        raise NameError
    except NameError:
        NameError(message)


if __name__ == "__main__":
    raise_exception_msg("Beautiful Error msg ")
