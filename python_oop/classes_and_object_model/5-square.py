#!/usr/bin/env python3
"""Going in-depth with getters and setters"""


class Square:
    """Class to represent a square"""
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                for _ in range(self.size):
                    print('#', end="")
                print()


if __name__ == "__main__":

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
