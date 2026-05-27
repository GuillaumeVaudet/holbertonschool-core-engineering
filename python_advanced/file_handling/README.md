# Python - File handling

This project introduce to Python's input/output mechanisms focusing on file manipulation. We will explore how to open, read, write, and append to files, while also understanding the importance of properly managing file ressources.

## Requirements
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.8.5**
- All files should end with a newl line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project is mandatory
- Our code should be PEP8 compliant (pycodestyle 2.14.0)
- All files must be executable
- The length of our files will be tested using `wc`

## Learning Objective
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement

## Scripts Descriptions
- [`read_file.py`](./read_file.py): The function reads a text file (`UTF8`) and print it to stdout
    - Prototype `def read_file(filename="")`
    - We must use the `with` statement
    - We don't need to manage `file permission` or `file doesn't exist` exceptions
    - Wa are not allowed to import any module
- [`write_file.py`](./write_file.py): The function writes a string to a text file (`UTF-8`) and returns the number of characters written:
    - Prototype: `def write_file(filename="")`
    - We must use the `with` statement
    - We don't need to manage file permission exceptions
    - Our function should create the file if doesn't exist
    - Our function should overwritte the content of the file if it already exists
    - We are not allowed to import any module
- [`append_write.py`](./append_write.py): The function appends a string at the end of a text file (`UTF-8`) and returns the number of characters added:
    - Prototype: `def append_write(filename="", text="")`
    - if the file doesn't exist, it should be created
    - We must use the `with` statement
    - We don't need to manage `file permission` or `file doesn't exist` exceptions
    - We are not allowed to import any module
## Authors
- Vaudet Guillaume [github profile](https://github.com/GuillaumeVaudet)