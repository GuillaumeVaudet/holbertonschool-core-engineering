#!/usr/bin/env python3
"""Abstract Shape Class and its Subclasses"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class named Shape"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Class named Circle that inherits from Shape"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Class named Rectangle that inherits from Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)
