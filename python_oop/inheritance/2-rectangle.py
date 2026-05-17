#!/usr/bin/env python3
"""First class for inheritance and polymorphism introduction"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represent a Rectangle inherit from BaseGeometry class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
