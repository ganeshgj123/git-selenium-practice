# -----------------------------------------------
# Dictionaries
# -----------------------------------------------

#  An empty dictionary
d = {}

# points
points = {'a': 1, 'b': 2, 'c': 3}

# dictionary with city and temperature (min and max) pair
temperatures = {"bangalore": (26, 29), "chennai": (29, 33), "delhi": (28, 35)}

# list inside the dictionary as values.
location = {'country': 'India', 'states': ['Karnataka', 'Andra', 'Kerala']}

# Nested Dictionary
prices = {'IBM': {'current': 90.1, 'low': 88.3, 'high': 92.7}, 'HP': {"current": 29.70, "low": 28.30, "high": 31.2} }

# --------------------------------------------------------------------
# doing a dictionary look-up
points['a']
points['d'] # raises KeyError exception

# using get method
points.get('a')

points.get('d')  # returns None
points('d', 0)  # returns zero
# --------------------------------------------------------------------

# adding new key to the dictionary
points['x'] = 1     # this creates a key "x" and assigns value 1 to it

# updating the existing key of the dictionary
points['a'] = points['a'] + 1       # increments the value of key "a" by 1

points['y'] = points['y'] + 1       # raises KeyError, as you are trying to fetch the current value of key 'y'
# and trying to add to the value. Since the key 'y' does not exist, python raises KeyError
# --------------------------------------------------------------------

# looping over the dictionary using "for" loop
# items() is a method on dict object, which returns a pair of key and value
for key, value in points.items():
    print(f"{key} ----> {value}")

# keys() is a method on dict object, which returns list of keys
for keys in points.keys():
    print(keys)

# values() is a method on dict object, which returns values of the dictionary
for values in points.values():
    print(values)
# ----------------------------------------------------------------------------
# Solution-1
# Count number of words in a sentence
# ----------------------------------------------------------------------------
sentence = 'hello world hello world welcome to python'
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# ----------------------------------------------------------------------------
# Solution-2 (using .get() method)
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
# ---------------------------------------------------------------------------
# Solution-3 (using .fromkeys() method)
"""
1. This creates a new dictionary using our colors as keys, with all values set to 0 initially.
2. This allows us to increment each key without worrying whether it has been set.
"""
word_count = {}
word_count = word_count.fromkeys(words)

for word in word_count:
    word_count[word] += 1
# ---------------------------------------------------------------------------
# Solution-4 (using defaultdict)
# ---------------------------------------------------------------------------
# using defaultDict

# 1. Creats a key if the key does not exist
# 2. Initialise the value to Zero in case of defaultdict of int's
# 3. Returns the value which is zero
# ---------------------------------------------------------------------------
from collections import defaultdict
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
# ---------------------------------------------------------------------------
# Counting number of characters in a string
word = 'abracadabraca'
char_count = {}
for letter in word:
    if letter in char_count:
        char_count[letter] += 1
    else:
        char_count[letter] = 1
# ---------------------------------------------------------------------------
# Alternate Solution (using .get() method)
word = 'abracadabraca'
char_count = {}
for letter in word:
    char_count[letter] = char_count.get(letter, 0) + 1
# ---------------------------------------------------------------------------
# Alternate Solution (using .fromkeys() method)
word = 'abracadabraca'
char_count = {}
char_count = char_count.fromkeys(word)

for letter in word:
    char_count[letter] = char_count[letter] + 1
# ---------------------------------------------------------------------------
# Counting number of vowels in a string
# ---------------------------------------------------------------------------
sentence = 'hello world welcome to python'
vowels = {}
for letter in sentence:
    if letter in 'aeiou':
        if letter in vowels:
            vowels[letter] +=1
        else:
            vowels[letter] = 1
# ---------------------------------------------------------------------------
# Counting occurances of word in the string (using defaultdict)
# ---------------------------------------------------------------------------
sentence = "hello world welcome to python hello hi hello hello"
word_count = defaultdict(int)
words = sentence.split()
for word in words:
    word_count[word] += 1
# ---------------------------------------------------------------------------
# Counting occurances of each character in the string (using defaultdict)
s = 'abracadabraca'
chr_count = defaultdict(int)
for c in s:
    chr_count[c] += 1
# ---------------------------------------------------------------------------
profile = defaultdict(list)     # One to Many Mapping

# 1. Creats a key if the key does not exist
# 2. Initialise the value to empty list in case of defaultdict of list
# 3. Returns the empty list

profile['language'].append('Java')
profile['language'].append('Python')
# ---------------------------------------------------------------------------
cities = [('India', 'Bangalore'),
          ('India', 'Chennai'),
          ('India', 'Delhi'),
          ('India', 'Kolkata'),
          ('USA', 'Dallas'),
          ('USA', 'New York'),
          ('USA', 'Chicago'),
          ('China', 'Bejing'),
          ('China', 'Shaingai')
          ]

dd = defaultdict(list)
for country, city in cities:
    dd[country].append(city)
# ---------------------------------------------------------------------------
# Composite Keys
# Dictionary key must be of Immutable Type. e.g
# Dict keys should always be Hashable. (All immutable objects are Hashable)
holidays = {
    (26, 1): 'Republic Day',
    (15, 8): 'Independance Day',
    (25, 6): 'Yoga Day'
}
# ---------------------------------------------------------------------------
# Deleting the key and value
d.popitem()      # Returns and deletes the last key/value pair in the dictionary
print(d.pop('age'))    # Returns and Deletes the mentioned key from the dictionary
# del employee['age']     # Deletes the Key 'age' and its value

# Merging Dictionaries
d1 = {'fname': 'steve', 'lname': 'jobs'}
d2 = {'age': 56, 'company': 'apple'}

d3 = {**d1, **d2}
# ------------------------------------------------------------------------------------------------------