#! /usr/bin/env python

def repeat(times=1):
    def inner(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return inner

@repeat(10)
def greet(name):
    print(f"Hello, {name}")

greet("Lorenzo")
