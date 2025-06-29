#! /usr/bin/env python

name = input("What is your name? ").strip().title()
if name == "":
    print("Coward!")
else:
    print(f"Hi, {name} and welcome to Python!")