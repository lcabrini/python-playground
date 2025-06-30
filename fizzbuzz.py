#! /usr/bin/env python

import sys

upto = 100
fizz = 3
buzz = 5

if len(sys.argv) > 1:
    try:
        upto = int(sys.argv[1])
    except:
        print(f"Not a valid value for upto: {sys.argv[1]}")
        sys.exit(1)
    if upto < 1:
        print(f"Not a valid value for upto: {sys.argv[1]}")
        sys.exit(1)
if len(sys.argv) > 2:
    try:
        fizz = int(sys.argv[2])
    except:
        print(f"Not a valid value for fizz: {sys.argv[2]}")
        sys.exit(1)
    if fizz < 1:
        print(f"Not a valid value for fizz: {sys.argv[2]}")
if len(sys.argv) > 3:
    try:
        buzz = int(sys.argv[3])
    except:
        print(f"Not a valid value for buzz: {sys.argv[3]}")
        sys.exit(1)
    if buzz < 1:
        print(f"Not a valid value for buzz: {sys.argv[3]}")
if len(sys.argv) > 4:
    print(f"Extra command-line argument: {sys.argv[4]}")
    sys.exit(1)

if fizz == buzz:
    print(f"fizz and buzz are both {fizz}")
    sys.exit(1)

if fizz > buzz:
    print(f"Fizz ({fizz}) is greater than buzz ({buzz})")
    sys.exit(1)

if fizz > upto:
    print("No fizzes, buzzes or fizzbuzzes will be printed")
    print(f"Might I recomend `seq {upto}` instead?")
    sys.exit(1)

for i in range(1, upto+1):
    if i % fizz == 0 and i % buzz == 0:
        print("fizz buzz")
    elif i % fizz == 0:
        print("fizz")
    elif i % buzz == 0:
        print("buzz")
    else:
        print(i)
