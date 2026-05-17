#!/usr/bin/env python3
"""Going in-depth with getters and setters"""


class Square:
    """Class to represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
            print(self)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def __str__(self):
        if self.size == 0:
            return ""

        square = ""

        square += "\n" * self.position[1]

        for i in range(self.size):
            square += (" " * self.position[0]) + ("#" * self.size)
            if i < self.size - 1:
                square += "\n"
        return square


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
