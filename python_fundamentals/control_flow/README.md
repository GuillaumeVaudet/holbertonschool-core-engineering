# Python_fundamentals - control_flow

This project is about how to manage and execute different code depending on conditions, loops, and logical conditions. This project focuses exclusively on control flow using: `if`, `elif`, `else`, comparaison operators, boolean logic, `while` loops, `for` loops with `range()`.

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
- No external librairies are allowed unless explicity requested
- No functions are allowed in this project
- No imports are allowed
- Outputmust match expected formatting exactly

## Usage
```bash
./positive_or_negative.py
```

## Learning Objectives
- Write conditional statements using `if`, `elif`, and `else`
- Use comparison and logical operators correctly
- Control repetition using `while` and `for` loops
- Reason about loop boundaries and iteration ranges
- Generate formatted output using numeric iteration
- Combine conditions and loops to produce deterministic output

## Scrips Descriptions
- [`positive_or_negative.py`](./positive_or_negative.py): Prints specific sentences depending on the sign of the generated number. This line is given for this exercice:
```python
number = __import__('random').randint(-10, 10)
```
- [`last_digit.py`](./last_digit.py): Prints specific sentences depending on the last digit of the generated number. THis line is given for this exercice:
```python
number = __import__('random').randint(-10000, 10000)
```
-[`print_alphabt.py`](./print_alphabt.py): Prints the lowercase except for `q` and `e`
-[`print_hexa.py`](./print_hexa.py): Prints numbers form 0 to 98 in decimal and hexadecimal
	- We can only use **one** `print` function with string format
	- We can only use **one loop** in our code
	- We are not allowed to store numbers or strings in a variable

