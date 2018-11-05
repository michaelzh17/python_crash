#!/usr/bin/env python3

from decorators import do_twice

@do_twice
def return_greeting(name):
    print("Creating {}".format(name))
    return "Hi shelly"

print(return_greeting("shelly"))

#print(hi_hi)
