# Python fundamentals - Exception Handling

This project is about how Python handles runtime errors and how to manage them using:
- `try/except`
- Specific exception types
- `else` and `finally` blocks
- Raising exceptions explicitly

## Requirements
- Correction will run on **Ubuntu 20.04 LTS**
- Python version used for correction: **Python 3.8.x**
- Every Python file must start exactly with:
```python
#!/usr/bin/env python3
```
- Every Python file must:
    - Be executable
    - End with a newline
    - Be PEP8 compliant (pycodestyle 2.14.0)
- No external librairies are allowed
- Unless explicitly stated, do not use broad except: blocks

## Learning Objectives
- Identify common runtime exceptions (TypeError, IndexError, ZeroDivisionError, KeyError)
- Use `try` and `except` blocks correctly
- Catch specific exception types rather than broad exceptions
- Use `else` and `finally` appropriately
- Raise exceptions explicitly when required
- Write functions that fail safely and predictably

## Scripts Descriptions
- [`safe_print_list.py`](./safe_print_list.py): The function prints x elements of a list
    - Prototype: `def safe_print_list(my_list=[], x=0)`
    - `my_list` can contain any type (integer, string, etc)
    - All elements must be printed on the same line followed by a new line
    - x represents the number of element to print
    - x can be bigger than the length of `my_list`
    - Returns the real number of elements printed
    - We have to use `try: / except:`
    - We are not allowed to import any module
    - We are notallowed to use `len()`