#!/usr/bin/env python3
"""Abstract Animal Class and its Subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class named Animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Class named Dog that inherits from Animal"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Class named Cat that inherits from Animal"""
    def sound(self):
        return "Meow"


if __name__ == "__main__":
    bobby = Dog()
    garfield = Cat()

    print(bobby.sound())
    print(garfield.sound())

    animal = Animal()
    print(animal.sound())
