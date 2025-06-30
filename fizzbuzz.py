#! /usr/bin/env python

import sys

upto = 100

if len(sys.argv) > 1:
    try:
        upto = int(sys.argv[1])
    except:
        print(f"Not a valid value for upto: {sys.argv[1]}")
        sys.exit(1)
    if upto < 1:
        print(f"Not a valid value for upto: {sys.argv[1]}")

for i in range(1, upto+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
