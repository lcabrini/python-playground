#! /usr/bin/env python

import os.path
import sys

prog = os.path.basename(sys.argv[0])
print(f"Program name: {prog}")

for i, a in enumerate(sys.argv[1:]):
    print(f"{i+1:>2}. {a}")