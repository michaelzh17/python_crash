#!/usr/bin/env python3
import functools


def _decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #do something before the function
        print("what did you say")
        value = func(*args, **kwargs)
        #do something after the function
        print("I said helllllo!")
        return value
    return wrapper

@_decorator
def wak():
    print("wak, wak")

wak()


