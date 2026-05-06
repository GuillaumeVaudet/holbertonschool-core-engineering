#!/usr/bin/env python3

i = ord('a')

while (i <= ord('z')):
    if (i != ord('e') and i != ord('q')):
        print(chr(i), end="")
    i += 1

print()
