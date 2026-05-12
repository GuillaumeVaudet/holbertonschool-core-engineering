#!/usr/bin/env python3

def safe_print_list(my_list=[], x=0):
    nb_of_elements_printed = 0
    for element in range(x):
        try:
            print(my_list[element], end="")
            nb_of_elements_printed += 1
        except IndexError:
            break
    print()
    return nb_of_elements_printed

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    
    nb_print = safe_print_list(my_list, 2)
    nb_print_2 = safe_print_list(my_list, 20)
    print(f"elements: {nb_print}")
    print(f"elements: {nb_print_2}")
