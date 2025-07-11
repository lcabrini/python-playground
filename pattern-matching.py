#! /usr/bin/env python

cmd = input("action: ").strip().lower()
exits = ("north", "west")
items = ["pen", "paper"]
match cmd.split():
    case ["go", direction] if direction in exits:
        print(f"Going {direction}")
    case ["go", _ as dir]:
        print(f"You cannot go {dir}")
    case ["look"]:
        print("You see a pen and a piece of paper.")
    case ["take", item] if item in items:
        print(f"Taking {item}")
    case ["take", _ as item]:
        print(f"You cannot take {item}")
    case "inventory" | "i":
        print(f"You don't have anything")
    case _:
        print("I don't understand you.") 
