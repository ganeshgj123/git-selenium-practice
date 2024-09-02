"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

sleep(3)

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

sleep(5)
"""
import math

# Count number of words in a sentence
"""
sentence = 'hello world hello hello world welcome to python python'

words = sentence.split()
word_count = {}
word_count = word_count.fromkeys(words,0)
for word in words:
    word_count[word] += 1
print(word_count)
"""

# Counting number of characters in a string

#word = 'abracadabraca'
"""
_char_count = { }

for letter in word:
    if letter not in _char_count:
        _char_count[letter] = word.count(letter)
print(_char_count)

char_count = { }
for letter in word:
    if letter in char_count:
        char_count[letter] += 1
    else:
        char_count[letter] = 1
print(char_count)

char_count_ = {}
for _letter in word:
        char_count_[_letter] = char_count_.get(_letter,0)+1
print(char_count_)"""

#using defaultDict
"""from collections import defaultdict

sentence = 'hello world hello world welcome to python'
words = sentence.split()

word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
print(word_count)"""



#Counting number of vowels in a string

#sentence = 'hello world welcome to python'
"""
vowels_count = {}

for letter in sentence:
    if letter in "aeiou":
        vowels_count[letter] = vowels_count.get(letter, 0) + 1
print(vowels_count)"""


#using from key
"""
vowels_count_ ={}
vowels_count_ = vowels_count_.fromkeys(sentence,0)

for letter_ in sentence:
    if letter_  in "aeiou":
        vowels_count_[letter_] += 1
    
print(vowels_count_)"""




#d1 = {'fname': 'steve', 'lname': 'jobs'}
#d2 = {'age': 56, 'company': 'apple'}
"""
d3 = {**d1, **d2}
print(d3)

d4 = d1 | d2
print(d4)

d1.update(d2)
print(d1)"""



#temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}
# for city, temperature in temperatures.items():
#     print(city,temperature)


# Deep Unpacking
"""for city, (_min, _max) in temperatures.items():
    print(city, _min, _max)"""

"""
least, *rest, maximum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( *rest)

*trailing, current = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(*trailing)

a, b, *c = range(1, 10)
print(a)"""


# data = ['IBM', 50, 91.1, (2019, 7, 17)]
"""name, *_, (year, *_) = data
print(name, *_, (year, *_))
"""

# Square Numbers in the list. Using List 4_Comprehensions

nums = [1, 2, 3, 4, 5]
"""
_nums = [ num**2 for num in nums ]

print(_nums)"""


# List of even numbers between range 1-50

"""even_nums = [i for i in range(1,51) if i%2==0]
print(even_nums)"""

# Returns a list containing all vowels in the given string
"""names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

vowel_names = [name for name in names if name[0] in "aeiou"]
print(vowel_names)
"""

# Filtering all the languages which starts with 'p'

"""languages = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
language_p = [language for language in languages if language[0] == "P"]
print(language_p)
language_p_ = [language_ for language_ in languages if language_.startswith("P")]
print(language_p_)
"""

# Names starting with consonents

"""names = ['laura', 'steve', 'bill', 'james', 'bob', 'greig', 'scott', 'alex', 'ive']

consonant_names = [name for name in names if name[0] not in "aeiou"]
print(consonant_names)
"""

# Filtering out those names which are less than 6 characters
"""names = ['apple', 'google', 'yahoo', 'gmail', 'flipkart', 'instagram', 'microsoft']

name_length_6 = [name for name in names if len(name)> 6]

print(name_length_6)"""


# Building a list of first_name and last_name from full_names
full_names = ["steve jobs", "bill gates", "john doe", "tim cook"]

"""first_name = [name.split()[0] for name in full_names ]
last_name = [name_.split()[1] for name_ in full_names]
print(first_name)
print(last_name)"""

"""first_name_ = []
last_name_ = []
for name in full_names:
    full_name = name.split()
    first_name, last_name = full_name
    first_name_.append(first_name)
    last_name_.append(last_name)
print(first_name_)
print(last_name_)"""

# Raise to the power of list index
"""a = [1, 2, 3, 4, 5]
for i in a:
    print( i ** a.index(i))
    
a__ = [i ** a.index(i) for i in a]
print(a__)

a_ = [value ** index for index,value in enumerate(a)]
print(a_)"""

# Build a list of tuples with string and its length pair
"""names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
name_length = []
for name in names:
    name_length.append((name, len(name)))
print(name_length)

name_length_ = [(name, len(name))for name in names]
print(name_length_)"""


# Build a list with only even length string
"""names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
names_ = [name for name in names if len(name)%2 == 0]
print(names_)
"""

# Generating List of PI values
"""import math

pi_list = [round(math.pi, n) for n in range(1, 6)]
print(pi_list)
"""

# List comprehension to sum the factorial of numbers from 1-5
from  math import factorial

"""a = [1, 2, 3, 4, 5]
a_ =[]
for num in a:
    a_.append(math.factorial(num))
print(sum(a_))

a__ = [math.factorial(num) for num in a]
print(sum(a__))"""

# Reverse the item of a list if the item is of odd length string
"""names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
names_ = [ name[::-1] for name in names if len(name) %  2 != 0 ]
print(names_)"""


# Reverse the item of a list if the item is of odd length string otherwise keep the item as is!.
"""names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

reversed_odd_names__ = [ name[::-1] if len(name) % 2 != 0 else name for name in names ]
print(reversed_odd_names__)
"""
"""
def reverse_string(name):
    if len(name) % 2 != 0:
        return name[::-1]
    else:
        return name

reversed_odd_names_ = [reverse_string(name) for name in names]
print(reversed_odd_names_)
"""

#reverse the item in the list if its of string type

"""data = ['hello', 123, 1.2, 'world', True, 'python']
reverse_string = [item[::-1] if isinstance(item,str) else item for item in data ]
print(reverse_string)"""


# Building a list of prime numbers from 1-50.

"""
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

prime_numbers = [number for number in range(2,51) if is_prime(number)]
print(prime_numbers)"""








"""def infinite_prime(number):
    if number > 1:
        for i in range(2, number//2 + 1):
            if number % i == 0:
                return False
        return True
    return "nothing"

for i in range (10):
    if infinite_prime(i):
        print(i)
"""





#infinite prime numbers
"""

def prime():
    num = 1
    while True:
        if num > 1:
            for i in range(2, num // 2 + 1):
                if num % i == 0:
                    break
            else:
                yield num

        num += 1


res = prime()
print(next(res))
print(next(res))

"""




"""def even_nums(iterable):
    evens = []
    for num in iterable:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(even_nums(list(range(10))))
"""




def even_nums(iterable):
    for num in iterable:
        if num % 2 == 0:
            yield num

# result  = even_nums(list(range(10)))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# for i in result:
#     print(i)

#
# result  = even_nums(list(range(10)))
# for i in result:
#     print(i)
# print(next(result))
#



def even():
    num = 0
    while True:
        if num % 2 == 0:
            yield num
        num += 1


print(even())
result = even()

print(next(result))
print(next(result))





