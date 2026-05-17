#!/usr/bin/env python3
"""Going in-depth for private attributes"""


class Square:
    """Class to represent a square"""
    def __init__(self, size):
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
