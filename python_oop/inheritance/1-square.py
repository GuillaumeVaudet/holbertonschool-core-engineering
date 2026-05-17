#!/usr/bin/env python3
"""First class for inheritance and polymorphism introduction"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """This class represent a Rectangle inherit from BaseGeometry class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
