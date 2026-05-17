#!/usr/bin/env python3
"""Base file for inheritance project into the Holberton school cursus"""


class BaseGeometry:
    """This class represents a foundational concept for geometric shapes"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
