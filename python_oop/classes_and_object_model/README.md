# Python - Classes & Object Model

This project is about how to organize data and logic with Object-Oriented Programming (OOP). The goal of this project is to build a solid understanding of the **Python object model**, which is the foundation for more advanced concepts such as **inheritance, polymorphism, and abstract classes** that will be explored in later projects.

## Requirements
- The development environment used for evaluation is **Ubuntu 20.04**
- Python version used for correction:**Python 3.8.x**
- All Python files must be executable
- The first line of all Python files must be:
```python
#!/usr/bin/env python3
```
- All files must end with a new line
- Code must follow **PEP8 style guidelines**
- All modules, classes, and functions should include **clear and concise documentation strings**
- No external librairies may be imported unless explicitly allowed
- All scripts must behave exactly as specified in the task instructions

## Learning Objectives
- Explain the difference between a **class** and an **instance**
- Create classes that model simple entities
- Define and initialize instance attributes using `__init__`
- Implement instance methods that operate on object state
- Apply basic **encapsulation principles**
- Validate input when constructing objects
- Control access to internal attributes
- Impelment string representations of objects using special methods
- Design simple classes that model real-world concepts

## Scripts Descriptions
- [`0-square.py`](./0-square.py): Contains a class named `Square` that represents a square (for this first version, the class does not need to contain any attributes or methods.)
- [`1-square.py`](./1-square.py): Contains a class `Square` with:
    - A private instance attribute `size`
    - The size must be set when the object is created
- [`2-square.py`](./2-square.py): Add validations to the `size` attribute on the `Square` class
    - `size` must be an integer, otherwize raise a `Typerror` exception with the message `size must be an integer`
    - `size` must be grater than or equal to 0. Otherwize raise a `ValueError` exception with the message `size must be >= 0`
- [`3-square.py`](./3-square.py): Add an instance method `area(self)` to the `Square` class that return the area of the square based on it's `side` length
- [`4-square.py`](./4-square.py): Add getters and setters for the `size` attribute in the `Square` class
- [`5-square.py`](./5-square.py): Add a public instance method `def my_print(self)` that prints in stdout the square with the character `#`. If size is equal to 0, print an empty line
- [`6-square`](./6-square.py): Add an implement the special method `__str__()`
    - Private instance attrivute: `position`:
        - Property `def position(self)`: to retrieve it
        - Property setter `def position(self, value)`: to set it
            - Position must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with message `position must be a tuple of 2 positive integer`
    - Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0,0))`
    - Public instance metho: `def my_print(self)`: that prints in stdout the square with character #:
        - If `size` is equal to 0, print an empty line
        - `position` should be use by using space
    - Printing a Square instance should have the same behavior as my_print()

## Authors
- Vaudet Guillaume [github profile](https://github.com/GuillaumeVaudet)