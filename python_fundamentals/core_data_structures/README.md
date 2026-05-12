# Python_fundamentals - core_data_structures

This project is about core built-in data structures and the reasoning skills needed to choose and use them correctly:
- **Lists** for ordered, mutable sequences
- **Tuples** for ordered, immuable groupings
- **Sets** for unique elements and set operations
- **Dictionaries** for key-value mappings

## Requirements
- Correction will run on **Ubuntu 20.04 LTS**
- Python version used for correction: **Python 3.8.x**
- Every Python file must start exactly with:
```python
#!/usr/bin/env python3
```
- Every Python file must:
	- Be executable
	- End with a new line
	- Be PEP8 compliant (pycodestyle 2.14.0)
- No external librairies are allowed
- Unless explicity stated otherwise, do not import modules

## Usage
```bash
./print_list_integer.py
```

## Learning Objectives
- Iterate over lists and matrices and produce exact, formatted output
- Access and modify list elements safely without raising unexpected errors
- Create new collections without mutating the original input when required
- Use tuples to return multiple values in a clear, consistent way
- Use sets to compute intersections and symmetric differences
- Use dictionaries to add, update, and query key-value data
- Reason about edge cases such as empty inputs, missing keys, and repeated values

## Scripts Descriptions
- [`print_list_integer.py`](./print_list_integer.py): The function prints all integers of a list.
	- Prototype: `def print_list_integer(my-list=[])`
	- Format: one integer per line
	- We may assume every element of my_list is an integer
	- ⚠️ important note: We are expected to explicitly format integers using `:d` in our print statement. Even if our function works correctly without it, most of the automated checks will fail if `:d` is not used.
- [`element_at.py`](./element_at.py): The function retrieves an element from a list like in C.
	- Prototype: `def element_at(my_list, idx)`
	- If `idx` is negative or out of range, return `None`
	- Otherwise, return the element at position `idx`
- [`replace_in_list`](./replace_in_list.py): The function replaces an element of a list at a specific position
	- Prototype: `def replace_in_list(my_list, idx, element)`
	- If `idx` is negative or out of range, return the original list unchanged
	- Othewise, replace the element at position `idx` with element and return the list
- [`print_matrix_integer.py`](./print_matrix_integer.py): The function prints a matrix of integers
	- Prototype: `def print_matrix_integer(matrix=[[]])`
	- `matrix` is a list of lists (2D list)
	- Format each row on its own line
	- Values in a row must be separated by a signle space
- [`add_tuple.py`](./add_tuple.py): The function adds two tuples
	- Prototype: `def add_tuple(tuple_a=(), tuple_b=())`:
	- Return a new tuple with exactly two integers
	- Treat missing values as 0
	- Ignore values beyond the first two
- [`common_elements.py`](./common_elements.py): The function returns a set of common elements in two sets
	- Prototype: `def common_elements(set_1, set_2)`
	- Return a **new** set containing only elements present in both `set_1` and `set_2``
- [`update_dictionary.py`](./update_dictionary.py): The function replaces or adds a key/value pair in a dictionary
	- Prototype: `def update_dictionary(a_dictionary, key, value)`
	- if key already exists, replace its value
	- if key does not exist, create it
	- Return the (updated) dictionary
- [`best_score.py`](./best_score.py): The function returns the with the biggest integer value
	- Prototype: `def best_score(a_dictionary)`
	- We may assume that all values are integers
	- If a_dictionary is None or empty, return None
	- We may assume all values are different