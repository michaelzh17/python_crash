#!/usr/bin/env python3

from decorators import do_twice

@do_twice
def greet(name):
    print("hello {}".format(name))

greet("Django")
