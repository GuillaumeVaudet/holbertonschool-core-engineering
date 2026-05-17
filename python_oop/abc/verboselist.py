#!/usr/bin/env python3
""" Extending the Python List"""


class VerboseList(list):
    """Class named VerboseList that inherits from list"""
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        super().extend(items)
        print("Extended the list with {} items.".format(len(items)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item


if __name__ == "__main__":
    vl = VerboseList([1, 2, 3])
    vl.append(4)
    vl.extend([5, 6])
    vl.remove(2)
    vl.pop()
    vl.pop(0)