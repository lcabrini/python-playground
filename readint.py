#! /usr/bin/env python

import sys

def readint(prompt):
    while True:
        s = input(f"{prompt}: ")
        try:
            i = int(s)
            return i
        except ValueError:
            print(f"Not a valid integer: '{s}'. Try again.", file=sys.stderr)

a = readint("Enter an integer")
b = readint("Enter another integer")
c = a + b
print(f"{a} + {b} = {c}")

