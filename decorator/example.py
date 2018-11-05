#!/usr/bin/env python3

def my_decorator(func):
    def wrapper():
        print("something happening before the function")
        func()
        print("something happening after the function")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()


