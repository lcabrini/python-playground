#! /usr/bin/env python

import os.path
import sys

def pascal_at(row, col):
    if col == 1 or col == row:
        return 1
    else: 
        return pascal_at(row-1, col-1) + pascal_at(row-1, col)

prog = os.path.basename(sys.argv[0])
if len(sys.argv[1:]) != 2:
    print(f"usage: {prog} ROW COL")
    sys.exit(1)

try:
    row = int(sys.argv[1])
except ValueError:
    print(f"Value for row is not a valid integer: {sys.argv[1]}")
    sys.exit(1)

try:
    col = int(sys.argv[2])
except ValueError:
    print(f"Value of col is not a valid integer: {sys.argv[2]}")
    sys.exit(1)

if row < 1:
    print("Row cannot be less than 1")
    sys.exit(1)

if col < 1:
    print("Col cannot be less than 1")
    sys.exit(1)

if col > row:
    print("Col cannot be greater than row")
    sys.exit(1)

print(pascal_at(row, col))
