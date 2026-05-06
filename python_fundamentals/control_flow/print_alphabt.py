#!/usr/bin/env python3

for i in range(97, 123):
    if i != ord('e') and i != ord('q'):
        print("{}".format(chr(i)), end="")
    i += 1

print()
