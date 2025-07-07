#! /usr/bin/env python

import random

def min_and_max(nums):
    min_value = nums[0]
    max_value = nums[0]

    for num in nums[1:]:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return (min_value, max_value)

nums = [random.randint(1, 100) for x in range(0, 10)]
min_value, max_value = min_and_max(nums)
print("Using min_and_max function:")
print(f"  max: {max_value}")
print(f"  min: {min_value}")

bi_min_value = min(nums)
bi_max_value = max(nums)
print("Using built-ins:")
print(f"  max: {bi_max_value}")
print(f"  min: {bi_min_value}")

