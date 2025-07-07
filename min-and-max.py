#! /usr/bin/env python

import random

nums = [random.randint(1, 100) for x in range(0, 100)]
min_value = 0
max_value = 0
started = 0

for num in nums:
    if not started:
        min_value = num
        max_value = num
        started = True
        continue

    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print(f"Max: {max_value}")
print(f"Min: {min_value}")