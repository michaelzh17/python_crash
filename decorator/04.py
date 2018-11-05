import functools

def _decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("do something before the function....")
        value = func(*args, **kwargs)
        print("do something after the function...")
        return value
    return wrapper

@_decorator
def sayhello(name):
    print("hello, {}".format(name))


sayhello("Josephy")
