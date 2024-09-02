# _demo.py
from time import sleep

def delay(some_func):
    def wrapper(*args):
        sleep(5)        # extra functionality
        return some_func(*args) # callback function is getting invoked
    return wrapper

@delay      # add = delay(add)
def add(a, b):
    return a + b

@delay      # sub = delay(sub)
def sub(a, b):
    return a - b

@delay      # mul = delay(mul)
def mul(a, b, c):
    return a * b * c

@delay      # greet = delay(greet)
def greet():
    return "hello world"

