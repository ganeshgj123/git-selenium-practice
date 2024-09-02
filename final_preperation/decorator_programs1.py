#find the number of args passed to a function
"""
def adder(func):
    def wrapper(*args,**kwargs):
        print(f"number of args of {func.__name__} : {len(args)}")
        return func(*args,**kwargs)
    return wrapper

@adder
def addition(a,b,c):
    return a+b+c

print(addition(2,5,6))
"""
import time

#reverse a string using decorator


"""
def reversed_str(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result[::-1]
    return wrapper


@reversed_str
def str_reverse(some_string):
    return some_string

print(str_reverse("python"))
"""


#write a decorator to execute a function 3 times
"""
def multiplier(func):
    def wrapper(*args,**kwargs):
        for i in range(1,4):
            result = func(*args,**kwargs) * i
            print(result)
    return wrapper


@multiplier
def number_to_multiply(num):
    return num

print(number_to_multiply(3))


def decorator(func):
    def wrapper(*args,**kwargs):
        for _ in range(3):
            print( func(*args,**kwargs))
    return wrapper

@decorator
def some_func():
    return "something"

some_func()
"""


#write a decorator to count the no of function calls

"""
d = {}
def count_decorator(func):
    def wrapper(*args,**kwargs):
        key = func.__name__
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
        print(f"{key} is called {d[key]} times")
        print(d)
        return func(*args,**kwargs)
    return wrapper


@count_decorator
def some_func():
    print("python interview")

@count_decorator
def other_func():
    print("selenium interview")

some_func()
some_func()
some_func()

other_func()
other_func()
other_func()
other_func()
"""

#using default dict
"""
from collections import defaultdict
d = defaultdict(int)

def count_decorator(func):
    def wrapper(*args,**kwargs):
        key = func.__name__
        d[key] += 1
        print(f"{key} is called {d[key]} times")
        print(d)
        return func(*args,**kwargs)
    return wrapper


@count_decorator
def some_func():
    print("python interview")

@count_decorator
def other_func():
    print("selenium interview")

other_func()
other_func()

some_func()
some_func()
some_func()
"""



#decorator that accepts only positional arguements

"""
def positional_args(func):
    def wrapper(*args):
        return func(*args)
    return wrapper

@positional_args
def addition(a,b):
    return a + b

print(addition(a=2,b=3))
"""



##decorator to convert a string output of a function to uppercase
"""
def upper_case(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs).upper()
        return result
    return wrapper

@upper_case
def some_str():
    return "python"

print(some_str())
"""



#decorator that accepts only keyword arguements
"""
def keyword_args(func):
    def wrapper(**kwargs):
        return func(**kwargs)
    return wrapper

@keyword_args
def multiplication(a,b,c):
    return a * b * c

print(multiplication(a=2,b=3,c=4))
"""


#decorator that reverses the output of a function only if the output is a sequence(list, str, tuple)
"""
def reverse_sequence(func):
    def wrapper(args,**kwargs):
        if not isinstance(args,(str,list,tuple)):
            raise TypeError("only sequences are accepted")
        return func(args,**kwargs)[::-1]
    return wrapper

@reverse_sequence
def sequence_to_reverse(sequence):
    return sequence

print(sequence_to_reverse(123))
# print(sequence_to_reverse(123))
"""

#decorator that creates a dictionary of arguments passed to a function and their result pairs

"""
d = {}
def create_dictionary(func):
    def wrapper(*args,**kwargs):
        if args not in d:
            d[args] = func(*args,**kwargs)
        return d
    return wrapper

@create_dictionary
def some_func(a,b,c):
    return a * b * c

print(some_func(2,5,6))
"""

######### parameterized decorators
"""
def delay_time(delay_time):
    def delay_decorator(func):
        def wrapper(*args,**kwargs):
            print(f"waiting for {delay_time}secs")
            time.sleep(delay_time)
            start = time.time()
            result = func(*args,**kwargs)
            end = time.time()
            elapsed_time = end - start
            print(f"time delay : {elapsed_time}" )
            return result
        return wrapper
    return delay_decorator

@delay_time(5)
def some_func():
    return "nfbsd"

print(some_func())
"""




"""
def type_validator(*types):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for value_, type in zip(args,types):
                if not isinstance(value_,type):
                    raise TypeError("enter valid types")
            return func(*args,**kwargs)
        return wrapper
    return decorator

@type_validator(int,int)
def subtract(a,b):
    if a > b:
        return a - b
    return b - a

print(subtract(2,6))
"""

