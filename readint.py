#! /usr/bin/env python

import sys

def even_validator(n):
    if n % 2 != 0:
        print(f"{n} is not an even integer. Try again")
        return False
    return True

def odd_validator(n):
    if n % 2 == 0:
        print(f"{n} is not an odd integer. Try again.")
        return False
    return True

def max_validator(max):
    def validator(n):
        if n > max:
            print(f"{n} is greater than {max}. Try again.")
            return False
        return True
    return validator

def range_validator(min, max):
    def validator(n):
        if n < min or n > max:
            print(f"{n} is not in the range ({min}-{max}). Try again.")
            return False
        return True
    return validator

def readint(prompt, validators=None):
    while True:
        s = input(f"{prompt}: ")
        try:
            i = int(s)
        except ValueError:
            print(f"Not a valid integer: '{s}'. Try again.", file=sys.stderr)
            continue

        valid = True
        if type(validators) in (list, tuple):
            for validator in validators:
                if not callable(validator):
                    raise TypeError("validators must be functions")
                if not validator(i):
                    valid = False
                    break
        elif callable(validators):
            if not validators(i):
                valid = False
        elif validators in None:
            pass
        else:
            raise TypeError("validators must be functions")

        if not valid:
            continue

        return i

a = readint("Enter an even integer", validators=even_validator)
b = readint("Enter an integer (max 10)", validators=max_validator(10))
c = readint("Enter an odd integer in the range (5-13)", validators=(odd_validator, range_validator(5, 13)))
try:
    d = readint("Enter an integer (this should fail)", validators="x")
except Exception as e:
    print(f"Something went wrong: {e}")

e = a + b + c
print(f"{a} + {b} + {c} = {e}")

