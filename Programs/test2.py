#write a program to create a  dictionary of character and its nummber of occurances

"""word = "occurances"
char_count= {}
for i in word:
    char_count[i] = word.count(i)

print(char_count)"""

"""char_count = {}
for char in word:
    char_count[char] = char_count.get(char,0) +1
print(char_count)"""

"""
char_count = {}
char_count = char_count.fromkeys(word,0)

for char in word:
    char_count[char] = word.count(char)
print(char_count)
"""

"""
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] =1
print(char_count)
"""

#create a list of the words starting with vowels in the given sentence

"""sentence = "Python follows a set of rules to determine the truth value of an object"
words = sentence.split()
vowel_words = []
"""
"""for word in words:
    if word.startswith(("a","e","i","o","u")):
        vowel_words.append(word)
print(vowel_words)"""

"""
for word in words:
    if word[0] in "aeiou":
        vowel_words.append(word)
print(vowel_words)
"""

#create a dictionary of vowels and number of occurances of each vowels
"""
sentence = "because these operators behave differently"

vowel_count = {}

for char in sentence:
    if char in "aeiou":
        vowel_count[char] = sentence.count(char)
print(vowel_count)"""


"""
for char in sentence:
    if char in "aeiou":
        if char in vowel_count:
            vowel_count[char] += 1
        else:
            vowel_count[char] = 1
print(vowel_count)
"""























############################################################################################################################
#check if the i terable is empty
"""lst = []
print(len(lst) == 0)

if len(lst) == 0:
    print("iterable is empty")
else:
    print("not empty")"""

#greatest of 3 numbers


"""
lst = [10, 50, 20]
maxx = lst[0]

for item in lst:
    if item > maxx:
        maxx = item
print(maxx)
"""
"""
lst.sort(reverse=True)
print(lst[0])
"""

"""
if lst[1] < lst[0] > lst[2]:
    print(f"{lst[0]} is greater")
elif lst[0] < lst[1] > lst[2]:
    print(f"{lst[1]} is greater")
else:
    print(f"{lst[2]} is greater")
    """


#converting upper to lower and vice versa

letter = "F"
"""
if letter.islower():
    print(letter.upper())
elif letter.isupper():
    print(letter.lower())
else:
    print("nothing")
    """

"""
if ord(letter) in range(ord("a"),ord("z")+1):
    print(chr(ord(letter) - 32))
elif ord(letter) in range(ord("A"),ord("Z")+1):
    print(chr(ord(letter) + 32))
else:
    print("nothing")
"""






#check if entered character is vowel or not

"""letter = input("enter the character: ")
if letter in "aeiouAEIOU":
    print("vowel")
else:
    print("not vowel")
"""


#check if entered character is vowel or not, if it is vowel then create a dictionary with char and its ascii value pair
"""
s = "character"
char ="a"
char_ascii = {}
if char in s:
    if char in "AEIOUaeiou":
        char_ascii[char] = ord(char)
        print(char_ascii)
    else:
         print("not an vowel")
"""



#check if the given number is even or odd

"""number = 56

if number % 2 == 0:
    print("even")
else:
    print("odd")"""

"""
def even_number(number):
    if number % 2 == 0:
        return "even number"
    return "Odd number"
print(even_number(56))
"""

#check whether the string is palindrome or not
"""
some_string = "mom"
if some_string == some_string[::-1]:
    print("palindrome")
else:
    print("not a palidrome")

"""

"""
def palindrome_string(some_string):
    reversed_string = ""
    for char in some_string:
        reversed_string = char + reversed_string
    return reversed_string
word = "OYO"

if palindrome_string(word) == word:
    print("palindrome")
else:
    print("not a palindrome")
"""




#check if the key is present, if present then increment or initialize the value to 1

"""
lst =["a","b","c","d"]
key ="c"
value_increment = {}
value_increment = value_increment.fromkeys(lst,1)

if key in value_increment:
    value_increment[key] += 1
    print(value_increment)
else:
    print("nothing")
"""


#check if the given value is string or not
"""
some_string = "adsadf"

if isinstance(some_string,str):
    print(f"{some_string} value is string")
else:
    print(f" {some_string} is not a string")
"""


#check if the integer is palindrome or not

# number = 564
"""
if str(number) == str(number)[::-1]:
    print("palindrome")
else:
    print("not a palindrome")
"""

"""
if str(number)=="".join(reversed(str(number))):
    print("palidrome")
else:
    print("not a palindrome")
    """


#check if the integer is prime or not

"""
def prime(num):
    if num>0:
        for i in range(2,num//2 + 1):
            if num % i == 0:
                return False
        return True
    return "less than 0"
    

print(prime(14))
"""

#fibonacci series
"""a= [0,1]

for i in range(1,15):
    a.append(a[-1]+a[-2])
print(a)
"""




#factorial
"""
def factorial(num):
    if num <= 0 :
        return 1
    else:
        for i in range(1,num):
           num = num * i
        return num
print(factorial(6))

"""


#check if the integer is palindrome or not
"""
num = 457
num1 = num

rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10


if rev == num1:
    print(f" {rev}: number is palindrome")
else:
    print(f" {rev}: not a palindrome")
"""


"""
def palidrome_number(num):
    rev = 0
    num1 = num

    while num > 0:
      rem = num % 10
      rev = rev * 10 + rem
      num //= 10
    if rev == num1:
        return True
    else:
        return False

print(palidrome_number(858))
"""


#check if the given character is number or alphabet or special character
"""
char = "A"

if char.isdigit():
    print("its a digit")
elif char.isalpha():
    print("its an alphabet")
else:
    print("special character")
    
    """
import string

#char = "~"
"""
if ord(char) in (range(ord("A"),ord("Z")+1) , range(ord("a"),ord("z")+1)):
    print("its an alphabet")
elif ord(char) in range(ord("0"),ord("9")+1):
    print("its a digit")
elif char in string.punctuation:
    print("special character")
else:
    print("whitespace")
    """
# check if the given number is perfect square or not







prices = {"mobile": 1000, "laptop" : 1238, "tablet" : 700, "television" : 1500}

#print(sorted(prices.items(), key=lambda item:item[0][-1]))

places = {"mysore":"Karnataka", "pune" : "Maharashtra", "cochin": "Kerala"}

#print(sorted(places.items(), key=lambda item: len(item[0])))


#print(sorted(places.items(), key=lambda item: item[1][-1 ]))

#print(places.items())






#list of algorithms to practice

#list
#string
#sorting
#linked list
#arrays













#sentence = "python is a programming language and programming is fun"

# find the longest and smallest word in the sentence
"""
print(max(sentence.split(), key=len))
print(min(sentence.split(), key=len))
"""

## find the longest non repeated word in the sentence
"""
l = []
for item in sentence.split():
    if sentence.split().count(item) != 2:
        l.append(item)
print(max(l,key=len))

"""
# find all the longest words in the sentence
"""
sentence = " hello world today is a good day"

words = sentence.split()
for word in words:
    if len(max(words, key=len)) == len(word):
        print(word)
"""

#anagram or not

words = ["eat", "dear", "fear", "fare", "listen", "silent", "ate", "tea", "dare", "read"]


"""
anagram = {}

for word in words:
    key = "".join(sorted(word))

    if key not in anagram:
        anagram[key] = [word]

    else:
        anagram[key] += [word]

print(anagram)
"""
"""
from collections import defaultdict

anagram_ = defaultdict(list)


for word in words:
    key = "".join(sorted(word))
    anagram_[key].append(word)

print(anagram_)
"""




#check if the given string is starting with vowel or not


# s = "exit"

"""
if s.startswith(("a","e","i","o","u","A","E","I","O","U")):
    print(f"{s} starts with vowel")
else:
    print("it doesnt start with an vowel")
    """
"""
if s[0] in "aeiouAEIOU":
    print("starts with an vowel")
else:
    print("doesnt start with an vowel")
"""


#check if the given string is ending with vowel or not

s = "code"

"""
if s.endswith(("a","e","i","o","u","A","E","I","O","U")):
    print(f"{s} ends with vowel")
else:
    print("it doesnt end with an vowel")
"""
"""
if s[-1] in "aeiouAEIOU":
    print("ends with an vowel")
else:
    print("doesnt end with an vowel")

"""


#check if the list has even number of elements













# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, end=",")
# print()


num = 0
sum = 0

while num < 10:
    if num % 2 == 0:

        print(num, end=",")
    num += 1





# lower to upper string
def upper(word: str) -> str:

    return "".join(chr(ord(char) - 32) if "a" <= char <= "z" else char for char in word)



#########################################################################

#string wave of a given string

txt = "male"

"""
def wave(txt: str) -> list:
        
   return [
        txt[:letter_] + txt[letter_].upper() + txt[letter_ + 1 :]
        for letter_ in range(len(txt))
        if txt[letter_].isalpha()
    ]
"""
"""
for letter in range(len(txt)):
    if txt[letter].isalpha():
        print(txt[:letter] + txt[letter].upper() + txt[letter + 1:])
 
"""



##################################################################################################

#Title Case Conversion

def to_title_case(word: str) -> str:

    """
    Convert the first character to uppercase if it's lowercase
    """

    if "a" <= word[0] <= "z":
        word = chr(ord(word[0]) - 32) + word[1:]

    """
    Convert the remaining characters to lowercase if they are uppercase
    """
    for i in range(1, len(word)):
        if "A" <= word[i] <= "Z":

            word = word[:i] + chr(ord(word[i]) + 32) + word[i + 1 :]

    return word


def sentence_to_title_case(input_str: str) -> str:

    return " ".join(to_title_case(word) for word in input_str.split())


# print(sentence_to_title_case("aakash giri"))




















