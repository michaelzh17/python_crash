#!/usr/bin/env python3

from decorators import do_twice

@do_twice
def say_whee():
    print("whee!")

say_whee()

