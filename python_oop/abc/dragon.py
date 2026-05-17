#!/usr/bin/env python3
"""Mastering Mixins"""


class FlyMixin():
    """Mixin class named FlyMixin"""
    def fly(self):
        print("The creature flies!")


class SwimMixin():
    """Mixin class named SwimMixin"""
    def swim(self):
        print("The creature swims!")


class Dragon(FlyMixin, SwimMixin):
    """Class named Dragon that inherits from FlyMixin and SwimMixin"""
    def roar(self):
        print("The dragon roars!")


if __name__ == "__main__":
    dragon = Dragon()
    dragon.swim()
    dragon.fly()
    dragon.roar()
