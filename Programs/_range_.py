# STRINGS
# range(start, end, step)
# Start index is always included.
# End index is always excluded.

# Prints numbers from 0 to 4 (upto 5 but not including 5)
for num in range(0, 5):
    print(num)  # prints 0, 1, 2, 3, 4

# Prints numbers from 0 to 4 (num starts from zero if start index is omitted)
for num in range(5):
    print(num)  # Prints 0, 1, 2, 3, 4

# Prints every altrante numbers starting zero
for num in range(0, 10, 2):
    print(num)      # Prints 0, 2, 4, 6, 8

# Prints number from 10 to 1
# In the below example end index is zero. So python prints numbers from
# 10 to 1. End index excluded.
for num in range(10, 0, -1):
    print(num)      # Prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Prints number form 10 to 0
for num in range(10, -1, -1):
    print(num)      # Prints 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0

# Prints alternate numbers from 10 to 0.
for num in range(10, -1, -2):
    print(num)      # Prints 10, 8, 6, 4, 2, 0

# Prints "Python is awesome!!" 5 times
for i in range(5):
    print('Python is awesome!!')

for _ in range(5):
    print('Python is awesome!!')
# Since we are not making use of any loop variable inside for loop, we
# can simply give _ (underscore). _ is called throw away variable in Python.

#######################################################################
greeting = "hello world"
# Iterating over string using range function. (non pythonic style)
for index in range(0, len(greeting)):
    print(greeting[index])
   
# iterating over a string in reversed direction
greeting = "hello world"

for i in range(len(greeting)-1, -1, -1):
    print(greeting[i])

# Printing Index and Character using range function (not preferred method)
for index in range(0, len(greeting)):
    print(f" Character {greeting[index]} is at index {index}")

# Printing alterate characters of the string using range function (not preferred method)
for index in range(0, len(greeting), 2):
    print(greeting[index])

#######################################################################    
# Iterating over a string (Pythonic Style)
greeting = 'hello world'

for item in greeting:
    print(item)

# Getting index and item in a string (Pythonic Style)
for index, item in enumerate(greeting):
    print(f" Character {item} is at index {index}")
# ------------------------------------------------------------------------------
# Iterating over multiple string objects using zip function
s1 = 'hello'
s2 = 'world'

for c1, c2 in zip(s1, s2):
    print(c1, c2)

# Printing alternate characters of the string (Pythonic approach)
for c in greeting[::2]:
    print(c)

# Iterating through the List (pythonic approach)
for item in names:
    print(item)

# Prints the item and its corresponding index in the list (Pythonic approach)
for index, item in enumerate(names):    # enumerate returns a tuple of index, item pair
    print(index, item)

# Using range function (not preferred method)
for index in range(0, len(names)):
    print(names[index])

# Printing Index and Item using range function (not preferred method)
for index in range(0, len(names)):
    print(index, names[index])

# Printing alternate items of the list (Pythonic approach)
for name in names[::2]:
    print(name)

# Printing alternate items of the list using range function (not preferred method)
for index in range(0, len(names), 2):
    print(names[index])

# Iterating over a part of the list
for item in names[:4]:
    print(item)

for index, item in enumerate(names, start=1):   # Index starts from 1
    print(index, item)

# ------------------------------------------------------------------------
# Iterating over multiple lists simultaniously
# ------------------------------------------------------------------------
cities = ['Tokyo', 'Delhi', 'Shanghai', 'Sao Paulo', 'Mumbai']
population = ['38,001,000', '25,703,168', '23,740,778', '21,066,245', '21,042,538']

# Iterating through multiple list Non-Pythonic approach
for i in range(len(cities)):
    print(cities[i], population[i])

# Iterating through multiple list using zip function
for city, population in zip(cities, population):
    print(city, population)

# Iterating through multiple list with un-equal lengths using zip function
a = [1, 2, 3]
b = ['v', 'w', 'x', 'y', 'z']

for i in zip(a, b):
    print(i)    # Prints (1, 'v'), (2, 'w'), (3, 'x')
    # zip function stops at the shortest list

for i in zip_longest(a, b):
    print(i)    # Prints (1, 'v'), (2, 'w'), (3, 'x'), (None, y), (None, z)

for i in zip_longest(a, b, fillvalue='NA'):
    print(i)    # Prints (1, 'v'), (2, 'w'), (3, 'x'), ('NA', y), ('NA', z)

a = [1, 2, 3]
b = ['x', 'y', 'z']
c = ['alpha', 'beta', 'gamma']

for i in zip(a, b, c):
    print(i)    # Prints (1, 'x', 'alpha'), (2, 'y', 'beta'), (3, 'y', 'gamma')
# ------------------------------------------------------------------------------------
files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']
for file in files:
    if file.endswith('pdf'):
        print(file)
# ------------------------------------------------------------------------------------
for file in files:
    if file[-3:] == 'pdf':
        print(file)

filenames = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.py', 'apple.doc']
# Multiple conditions in startswith and endswith function
for filename in filenames:
    if filename.endswith(('txt', 'pdf')):   # filename either endswith txt or pdf
        # startswith and endswith can take tuple as an argument
        print(filename)
# ------------------------------------------------------------------------------------
files = ['youtube.txt', 'amazon.pdf', 'facebook.pdf', 'google.pdf', 'apple.doc']

# performing string related operations on each item of the list
# ------------------------------------------------------------------------------------
# prints upper case version of each item of the list
for item in files:
    print(item.upper())

# prints the type of each item of the list
for item in files:
    print(type(item))

# splits each of the list
for item in files:
    parts = item.split(".")
    print(parts)

# prints the item and its length
for item in files:
    print(f"the length of item {item} is {len(item)}")


