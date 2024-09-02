# _demo.py
from time import sleep
from time import time

def delay(some_func):
    def wrapper(*args):
        sleep(5)        # extra functionality
        return some_func(*args) # callback function is getting invoked
    return wrapper

def log(some_func):
    def wrapper(*args):
        print(f"You are calling: {some_func.__name__}")        # extra functionality
        return some_func(*args)     # orig (or callback function) func getting executed
    return wrapper


def _time(some_func):
    def wrapper(*args):
        start = time()      # Note down the current system time before executing callback function
        result = some_func(*args)       # callback function gets executed
        end = time()        # Note down the cureetn system time after executing callback function
        print(f"time elapsed : {end-start}")
        return result       # return the result of original or callback function
    return wrapper

@_time
def add(a, b):
    sleep(3)
    return a + b

@_time
def sub(a, b):
    sleep(5)
    return a - b

@_time
def mul(a, b, c):
    sleep(6)
    return a * b * c

@_time
def greet():
    sleep(1)
    return "hello world"




"""
from time import sleep,time



def delay(func):
    def wrapper(*args):
        start = time()
        result = func(*args)
        end = time()
        print(end-start)
        return result
    return wrapper

@delay
def add(a,b):
    sleep(5)
    return a+b

#add = delay(add)

print(add(1,2))

"""