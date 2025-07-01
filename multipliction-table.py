#! /usr/bin/env python

row = "    |"
for i in range(1, 13):
    row += f"{i:>4}|"
print(row)
print("----+" * 13)

for i in range(1, 13):
    row = f"{i:>4}|"
    for j in range(1, 13):
        row += f"{i*j:>4}|"
    print(row)