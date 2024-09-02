# Working with Strings.
# -------------------------------------------------------------------------------------------
"""String is a series of unicode characters enclosed between single/double/triple quotes"""
"""
1. We can use both single and double quotes for the strings.
2. If you have single quotes in the actual string, we can represent the original string in double quotes.
3. If the string actual string contains double quotes, we can use single quotes to represent the String.
4. A multiline string can be represented using triple quotes
"""

# Difference ways of constructing a string object
word = 'Hello World'

# string with zero length
word = ""   

# We can use Escape Charater as well (Not pythonic way)
sentence = 'Welcome to Python\'s world'

sentence = "Welcome to Python\"s world"

# actual string has a single quote
sentence = "Welcome to Python's world"

# actual string has a double quote
sentence = 'Welcome to Pythons"s world'

# multiline string
paragraph = """ this is a multiline string
hello world welcome to python programming
language
this is a new line
"""
# -------------------------------------------------------------------------------------------
word = 'Hello World'
# -------------------------------------------------------------------------------------------
# type is an inbuilt function, which returns the datatype of the
# variable or an object
# programatically get to know the data type of a variable
type(word)

"""
1. word is of type str and its value is "Hello world"
2. word is an instance of class str
3. word is a string object with value "Hello world"
4. Every object has "identity", "type" and "value".
5. word is a label which points to a string object.
"""
# -------------------------------------------------------------------------------------------
# len returns the length of the string
"""
len is a built-in funtion which returns the length of the given string
"""
len(word)
# -------------------------------------------------------------------------------------------
"""
dir is an inbuilt function, which returns a list of attributes 
that are attached to the object.
"""
dir(word)
# -------------------------------------------------------------------------------------------
"""
we can get information about a function using in-built function help()
e.g. help("hello".upper)
"""
help("hello".split)
# -------------------------------------------------------------------------------------------
# String Functions
# NOTE: ALL STRING FUNCTIONS RETURNS A NEW STRING AND WILL NOT MODIFY OR MUTATE THE EXISTING STRING.
# STRINGS ARE IMMUTABLE
# -------------------------------------------------------------------------------------------

# returns a new string with all characters in upper case
word.upper()

# returns a new string with all characters in lower case
word.lower()

# returns the number of occurances of the sub-string "l" in the bigger string
word.count('l')

# returns the number of occurances of sub-string "Hello" in the bigger string
word.count('Hello')

# returns the index of first occurance of sub-string "l"
word.find('l')

# returns the index of first occurance (lowest index) of sub-string "World" 
word.find('World')

# if the sub-string is not found, find() method returns negative one (-1)
word.find('Universe')

# returns the highest index (from right side) of occurance of sub-string "day"
"today is beautiful day".rfind("day")

# replaces "World" with "Universe" and returns a new string
word.replace('World', 'Universe')

# splits the string on whitespace and returns a list
word.split()

line = 'This is my string'
line.split('s')

# splits the string based on comma (,)
info = '560100,Bangalore,KA'
parts = info.split(',')

# space-delimit data
line = "Jun 03 22:58:18 farnsworth sshd[29386]: Failed password for invalid user root from 116.31.116.15 port 24544 ssh2"
parts = line.split()

# comma-delimit data
record = "2020-01-03,IN,India,SEARO,0,0,0,0"
parts = record.split(",")

# pipe-delimit data
record = "2017-06-01T07:43:07.481Z|host1099-99.testnetwork.local|filebeat|log|Jun  1 07:43:06 host1099-99.testnetwork.local sshd[26668]: Failed password for root from 123.183.209.136 port 37835 ssh2"

# returns True if the string starts with "Hello" otherwise returns False
word.startswith('Hello')

# returns True if the string ends with "World" otherwise returns False
word.endswith('World')

# strips leading and trailing whitespaces of the string
sentence = '           Hello world welcome to python               '
sentence.strip()

# joins each character or letter of the string with the delimiter provided
message = 'hello'
# Joins each character of the string using '-'
'-'.join(message)   

# Joins each character of the string using ','
','.join(message)
# --------------------------------------------------------------------------
# using "in" operator to check if the character is present in the string
# "in" is also called as membership operator
# --------------------------------------------------------------------------
greeting = "hello world"
"d" in greeting # (returns True)
"y" in greeting # (returns False)
"hello" in greeting # (returns True)
"hi" in greeting # (returns False)
# -------------------------------------------------------------------------------
# String Slicing
# -------------------------------------------------------------------------------
# my_message[start:stop:step]
word = 'Hello World'

#  H    e     l     l    o       W   o   r   l   d
#  0    1     2     3    4   5   6   7   8   9   10
# -11  -10   -9    -8   -7  -6  -5  -4  -3  -2   -1

print(word[0])        # Prints the character present at the 0th index
print(word[10])       # Prints the character present at the 10th index
printm(word[0:5])      # Prints Hello. Upto 5th character, but NOT INCLUDING the 5th
print(word[:5])       # Prints Hello.
print(word[6:])       # Prints World

# Negative Indexing
print(word[-1])      # Prints 'd'
print(word[-11])     # Prints 'H'
print(word[-4:])     # Prints 'World'
print(word[0:-6])    # Prints 'Hello'
print(word[2:-3])    # Prints 'llo Wo'

# Step
print(word[::2])      # Prints Every Alternate Characters
print(word[::-2])     # Prints Every Alternate Characters in reverse order
print(word[::-1])     # Prints the string in reversed order

# Print extension of the filename
name = 'Youtube.txt'
print(name[-3:])

# Print only filename
print(name[:-3])

# Printing only protocol in url
url = 'https://google.com'
print(url[:5])

# Print only domain
print(url[7:])
# ---------------------------------------------------------------------------------------
# String formatting.
# ---------------------------------------------------------------------------------------
name = "Steve"
age = 26
print("Hello {} you are {} years of age".format(name, age))

print("Hello {1} you are {0} years of age".format(name, age))

# using "f" strings
print(f"Hello {name} you are {age} years of age")
# ---------------------------------------------------------------------------------------
# handling characters with special meaning. (backslash characters)
# We can use either double backslash or prefix 'r' which stands for raw string or regular expression
print("C:\\testing\\newfolder")
print(r"C:\testing\newfolder")

