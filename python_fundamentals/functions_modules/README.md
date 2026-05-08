# Python_fundamentals - function & modularity

THis project is about function definition and return values, execution flow inside and outside functions, separation between printing and returning, how python executes a file, how importing a file affects execution, and how to reuse functions and variables across files.

## Requirements
- Correction will run on **Ubuntu 10.04 LTS**
- Python version used for correction: **Python 3.8.x**
- The first line of every Python file must be exactly:
```Python
#!/usr/bin/env python3
```

- All files must:
    - Be executable
    - End with a newline
    - Be PEP8 compliant (pycodestyle 2.14.0)
- No external librairies are allowed
- No use of `sys.argv` in this project
- Each task must follow its own constraints precisely

## Learning Objectives
- Define functions with parameters and return values
- Distinguish clearly between `print` and `return`
- Implement logic inside functions using conditionals and loops
- Understand how Python executes top-level code in a file
- Explain what `if __name__ == "__main__"` does and why it necessary
- Import functions from other files
- Import variables from other files
- Write scripts that behave correctly when executed and when imported

## Scripts Descriptions
- [`islower.py`](./islower.py): The function returns `True` if `c` is a lowercase letter and `False`otherwise
    - Task requirements:
        - We are not allowed to use built-in string methodes such as `.islower()`
        - We must use ASCII logic (`ord()`)
        - The function must return a boolean value
- [`uppercase.py`](./uppercase.py): The function prints the string in uppercase followed by a new line
    - Task requirement:
        - We are not allowed to use `.upper()`
        - We must use ASCII conversion (`ord()` and `chr()`)
        - The function must print the result directly
        - The function does not return a value
- [`print_last_digit.py`](./print_last_digit.py): The function must:
    - Print the last digit of `number`
    - Return the value of the last digit
    - The last digit must be positive