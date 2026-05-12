#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    nb_of_element_printed = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            nb_of_element_printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return nb_of_element_printed


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
