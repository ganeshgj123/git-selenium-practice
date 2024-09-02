

#find the numberof args passed to a function
"""def number_args(func):
    def wrapper(*args,**kwargs):
        print(f"number of args {len(args)}")
        return func(*args,**kwargs)
    return wrapper

@number_args
def count_args(a,b):
    print("arguements")

print(count_args(1,2))"""


#reverse a string using decorator
"""def reversed(func):
    def wrapper(*args,**kwargs):
        result =  func(*args,**kwargs)
        return result[::-1]
    return wrapper
@reversed
def reversed_string():
    return "hello"

print(reversed_string())"""





#write a decorator to execute a function 3 times
"""
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
function_count = {}
def decorator(func):
    def wrapper(*args,**kwargs):
        key = func.__name__
        if key not in function_count:
            function_count[key] = 1
        else:
            function_count[key] += 1
        return func(*args,**kwargs)

    return wrapper

@decorator
def add(a,b):
    return a+b

@decorator
def sub(a,b):
    return a-b

print(add(1,2))
print(add(3,2))
print(add(4,2))

print(sub(1,2))
print(sub(1,2))

print(function_count)
"""
#using default dict
"""
from collections import defaultdict

d= defaultdict(int)

def decorator(func):
    def wrapper(*args,**kwargs):
        key = func.__name__
        d[key] += 1
        return func(*args, **kwargs)
    return wrapper

@decorator
def add(a,b):
    return a+b

@decorator
def sub(a,b):
    return a-b

print(add(1,2))
print(add(3,2))
print(add(4,2))

print(sub(1,2))
print(sub(1,2))

print(d)
"""


#decorator that accepts only positional arguements

"""
def positional_args(func):
    def wrapper(*args,**kwargs):
        if len(kwargs) == 0:
            return func(*args,**kwargs)
        return 0
    return wrapper

@positional_args
def mul_func(a,b,c):
    return a*b*c

print(mul_func(1,2,3))
"""
"""
def positional_args(func):
    def wrapper(*args):
        return func(*args)
    return wrapper

@positional_args
def mul_func(a,b,c):
    return a*b*c

print(mul_func(1,2,3))
"""





#decorator to convert a string output of a function to uppercase
"""
def string_uppercase(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return wrapper

@string_uppercase
def some_string():
     return "something"

print(some_string())

"""



#decorator that accepts only keyword arguements

"""def positional_args(func):
    def wrapper(*args,**kwargs):
        if len(args) == 0:
            return func(*args,**kwargs)
        return 0
    return wrapper

@positional_args
def mul_func(a,b,c):
    return a*b*c

print(mul_func(a=1,b=2,c=3))"""

"""
def positional_args(func):
    def wrapper(**kwargs):
            return func(**kwargs)
    return wrapper

@positional_args
def mul_func(a,b,c):
    return a*b*c

print(mul_func(a=1,b=2,c=3))
"""




#decorator that reverses the output of a function only if the output is a sequence(list, str, tuple)
"""
def reverse_sequence(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        if isinstance(result,(str,tuple,list)):
            return result[::-1]
            # return sorted(result,reverse=True)
        return "Nothing"
    return wrapper
@reverse_sequence
def some_sequence(sequence):
    return sequence

print(some_sequence("ganesh"))
"""


#decorator that creates a dictionary of arguments passed to a function and their result pairs
"""
d ={}
def decorator(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        d[args] = result
        return d[args]

    return wrapper

@decorator
def mul_func(a,b,c):
    return a*b*c

@decorator
def add(a,b):
    return a+b
"""
#
# print(mul_func(1,2,3))
# print(mul_func(5,6,7))
# print(add(3,4))
#
# print(d)



#parameterised decorator
from time import sleep

def log(msg):
    def delay(func):
        def wrapper(*args,**kwargs):
            print(f"{msg} displayed")
            sleep(3)
            return func(*args,**kwargs)
        return wrapper
    return delay

@log("Hello python message")
def some_func():
    print("some message")

# some_func()



# type validator decorator

def type_validator(*types ):
        def decorator(func):
            def wrapper(*args):

                for value,type_ in zip(args,types):

                    if not isinstance(value,type_):

                        raise TypeError(f" {value} is not of {type_} type")

                return func(*args)
            return wrapper
        return decorator

@type_validator(int,int)
def add(a,b):
    return a + b

# print(add(2,4))



