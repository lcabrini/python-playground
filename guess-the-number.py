#! /usr/bin/env python

import random
import sys

LO = 1
HI = 100

def read_guess():
    while True:
        s = input("Your guess: ")
        try:
            n = int(s)
        except ValueError:
            print(f"Not a valid guess: '{s}'. Try again.")

        if n < LO or n > HI:
            print(f"Not in the valid range ({LO}-{HI}): {n}. Try again")
            continue

        return n

cheat_mode = False
if len(sys.argv) == 2 and sys.argv[1] == "cheat":
    cheat_mode = True

secret = random.randint(LO, HI)
if cheat_mode:
    print(f"CHEAT MODE ENABLED: {secret}")
guesses = 0
print(f"I'm thinking about a number between {LO} and {HI}. Try to guess it.")
while True:
    n = read_guess()
    guesses += 1
    if n > secret:
        print("Too high")
    elif n < secret:
        print("Too low")
    else:
        break

print("You did it! You guessed the right number.")
print(f"You needed {guesses} guess{'' if guesses == 1 else "es"}.")
