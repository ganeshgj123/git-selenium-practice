# _demo.py

# defined function
def greeting():
    # this is function implementation
    print("hello world")
    print("executing greeting function")
    print("hi there")

def greet():
    return "hello world"

def _greet(name):
    return f"hello {name}"

def add(a, b):
    return a + b

def greet(name="world"):
    return f"hello {name}"

def greeting(name, age, pay):
    return f"hello {name} you are {age} years of age and you get ${pay}"

def greeting(name, age=26, pay=500):
    return f"hello {name} you are {age} years of age and you get ${pay}"


def greet(name, debug=False):
    if debug:       # if debug == True
        print("You called greet function")
    return f"hello {name}"
        

def greet(name, reverse=False, debug=False):
    if debug:       # if debug == True
        print("You called greet function")
    if reverse:     # if reverse == True
        return f"hello {name[::-1]}"
    return f"hello {name}"


def spam(some_value):
    if some_value < 10:
        return "very low"
    if some_value > 10 and some_value < 20:
        return "average"
    if some_value == 10:
        return "correct guess"
    return [1, 2, 3, 4, 5]

def spam(some_value):
    if some_value < 10:
        print("very low")
    if some_value > 10 and some_value < 20:
        print("average")
    if some_value == 10:
        print("correct guess")
    return [1, 2, 3, 4, 5]


def greeting(name, age, pay):
    return f"hello {name} you are {age} years of age and you get ${pay}"

def greet(name, *, reverse=False, debug=False):
    if debug:       # if debug == True
        print("You called greet function")
    if reverse:     # if reverse == True
        return f"hello {name[::-1]}"
    return f"hello {name}"

# name can be either positional or keyword argument
# but reverse and dubug are mandatory keyword ONLY
def greet(name, *, reverse, debug):
    if debug:       # if debug == True
        print("You called greet function")
    if reverse:     # if reverse == True
        return f"hello {name[::-1]}"
    return f"hello {name}"


# all arguments are strictly keyword ONLY
def greet(*, name, reverse, debug):
    if debug:       # if debug == True
        print("You called greet function")
    if reverse:     # if reverse == True
        return f"hello {name[::-1]}"
    return f"hello {name}"

def greeting(*, name, age, pay):
    return f"hello {name} you are {age} years of age and you get ${pay}"

# arguments that are defined towards left of the "/" are mandatory positional ONLY
def greeting(name, /, *, age, pay):
    return f"hello {name} you are {age} years of age and you get ${pay}"

# all arguments in the below function defnition is strictly positional only
def greeting(name, age, pay, /):
    return f"hello {name} you are {age} years of age and you get ${pay}"


