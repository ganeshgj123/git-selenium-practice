#1. Write a program to find the length of the string without using inbuilt function (len)
from itertools import combinations
from re import findall
from time import sleep

s = "without"

"""str_len = findall(r"[a-zA-Z]",s)
print(len(str_len))
"""
"""count = 0
for i in s:
    count+=1

print(count)"""


#2. Write a program to reverse a string without using any inbuilt functions.

t = "program"

"""rev = ''
for i in t:
    rev = i + rev
print(rev)
"""

#print(t[::-1])


#3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".

r = "Hello World"
"""replace_str = r.split()
replace_str[1] = "Universe"

print(" ".join(replace_str))

"""
#print(r.replace("World","Universe"))


#4. How to convert a string to a list and vice-versa.

b = "convert"
"""print(list(b))

print("".join(list(b)))


"""


#5.Convert the string "Hello welcome to Python" to a comma separated string.

#print("Hello welcome to Python".replace(" ",","))

#p = "Hello welcome to Python"

#print(",".join(p.split()))

"""
f = ""
for i in p:
    if i == " ":
        f += ","
    else:
        f += i
print(f)
"""



#6. Write a program to print alternate characters in a string.

"""
x = "PycharmProjects"
print(x[1::2])

g = [j for i,j in enumerate(x) if i % 2 !=0]
print("".join(g))
"""
"""
for i , j in enumerate(x):
    if i % 2 != 0:
        g += j
else:
        g += ""
print(g)
"""


#7. Write a Program to print ascii values of the characters present in a string.

"""
k = "Program"
for i in k:
    print(ord(i),end=" ")

"""


#8. Write program to convert upper case to lower case and vice-versa without using inbuilt method.
"""
g = "SeleniumPython"

convert_case = ""

for i in g:
#    if "a" < i < "z":
    if ord(i) in range(ord("a"),ord("z")+1):
        convert_case = convert_case + chr(ord(i) - 32)
    elif ord(i) in range(ord("A"), ord("Z") + 1):
#    elif "A" < i < "Z":
        convert_case = convert_case + chr(ord(i) + 32)
    else:
        convert_case += i

print(convert_case)

"""



#9. Write program to swap two numbers without using 3rd variable.

"""a = 2
c = 3

a,c = c,a
print(a)
print(c)
"""

#10. Write program to merge two different lists.
"""
l1 = [1,2,3,4,5]
l2 = [6,7,8,9]

print(l1+l2)

l1.extend(l2)
print(l1)
"""

#11. Write program to read a random line in a file. (ex. 50, 65, 78th line)

"""def random_line(lineno):
    with open("sample.log") as file:
        for no,line in enumerate(file,start=1):
            if lineno == no:
                if line.strip():
                    print(line)

random_line(62)
"""



#50 Write a program to reverse the list as below

"""
words = ["hi", "hello", "python"]
reversed_list = [word[::-1]for word in words[::-1]]
print(reversed_list)

"""



#51 Write a program to update the tuple

"""
t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)
t1 = t1 + t2
print(t1)

"""


#52 Write a program to replace value present in nested dictionary.

"""
d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}

for key, value in d.items():
    if isinstance(value, dict):
        for i, j in value.items():
            if j == "nose":
                value[i] = "net"

print(d)
"""


#53 Write a program to count the number of white spaces in a file.

"""
with open("sample.log") as file:
    spaces = 0
    for line in file:
        for i in line:
            if i == " ":
                spaces += 1

print(spaces)
              """
"""
with open("sample.log") as file:
    spaces = 0
    for line in file:
            spaces += line.count(" ")

print(spaces)

"""



#54 Grouping anagrams
"""
words = ['eat', 'ate', 'tea', 'hello', 'silent', 'listen']

d = {}
for i in words:
    key = tuple(sorted(i))
    if key not in d:
        d[key] = [i]
    else:
        d[key].append("".join(i))

print(d)

"""


#59 Write a list comprehension to get a list of even numbers from 1-50

"""
print([i for i in range(1,50) if i % 2 == 0])
print(list(range(0,50,2)))
"""

#60 Find the longest non-repeated substring in the below string

sentence = "This is a Programming language and Programming is fun"


#longest_string = max(sentence.split(),key=len)
"""
s1 = []
for word in sentence.split():
    if sentence.split().count(word) != 2:
        s1.append(word)
print(max(s1,key=len))
"""



#61 Write a program to find the duplicate elements in the list without using inbuilt functions

"""
names = ['apple', 'google', 'apple', 'yahoo', 'google']
dup_name = []
non_dup = []


for name in names:
    if name not in non_dup:
        non_dup += [name]
    else:
        dup_name += [name]

print(dup_name)

"""


"""
d = {}

for name in names:
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1
print(d)

dup_list = []
for key,value in d.items():
    if value > 1:
        dup_list += [key]

print(dup_list)


"""



#62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions

"""

names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']

d = {}

for name in names:
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1
print(d)


"""


#63 Write a function to check if the number is Prime

"""

def prime_num(num):
    if num > 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True



print([n for n in range(1,51) if prime_num(n)])


"""




#65 Write a program to find the largest number in the list without using any inbuilt functions

"""
numbers = [10, 20,70,5, 30, 40, 50]

largest_num = numbers[0]

for i in numbers:
    if i > largest_num:
        largest_num = i

print(largest_num)


smallest_num = numbers[0]

for i in numbers:
    if i < smallest_num:
        smallest_num = i

print(smallest_num)

"""



#66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.


"""def get_last_digit(num):
    last_digit = num % 10
    return last_digit

print(get_last_digit(5452567))
"""
"""def get_last_digit(num):
    return str(num)[-2]

print(get_last_digit(1864868))
"""


#67 Write a program to find most common words in a given list.
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around',
'the',
'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
]
"""
from collections import Counter

d = {}

for word in words:
    count = 0
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
        count += 1


c = Counter(d)
print(c.most_common())

"""



"""
d = {}

for word in words:
    count = 0
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
        count += 1

print(d)

common_words = []

for i,j in d.items():
    if j > 1:
        common_words.append(i)

print(common_words)
"""


#68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number
# n and returns the last n elements from the given sequence, as a list.

"""
def tail(sequence,n):
    if isinstance(sequence,(str,tuple,list)):
        return [sequence[-n:]]
    return "invalid sequence"

print(tail(5486,4))


"""



#69 Write function named is_perfect_square that accepts a number and returns True if it's a
# perfect square and False if it's not.
"""l1 = []

def is_perfect_square(n):
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return True
        elif mid * mid < n:
            left = mid + 1
        else:
            right = mid - 1
    return False
print(is_perfect_square(36))

l = [24, 16,81,23,64]

for i in l:
    if is_perfect_square(i):
        l1.append(i)

print(l1)
"""


"""
def is_perfect_square(n):
    i = 1
    while i * i <= n:
        if i * i == n:
            return True
        i += 1
    return False
print(is_perfect_square(64))

"""
"""
from math import sqrt

def perf_sqr(n):
    sqr_num = sqrt(n)
    if sqr_num.is_integer():
        return "perfect square"
    return "not a perfect square"

print(perf_sqr(27))

"""



#70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.

"""
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail','gmail', 'gmail']

d = {}
for name in names:
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1

print(d)

l1 = []
for key, value in d.items():
     if value > 1:
         l1.append(key)

print(l1)

"""



#71 Write a program to count the number of occurrences of each word in a file.
"""
d = {}

with open("sample.log") as file:
    for line in file:
        if line.strip():
            for word in line.split():
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1

print(d)
"""

#program to count the no of lines in a file

"""
with open("sample.log") as file:
    count = 0
    for line in file:
        if line.strip():
            count += 1
print(count)
"""



#72 Write a program to count the number of occurrences of vowels in a file.
"""
d = {}
with open("sample.log") as file:
    for line in file:
        if line.strip():
            for letter in line:
                if letter in "aeiouAEIOU":
                    if letter not in d:
                        d[letter] = 1
                    else:
                        d[letter] += 1
print(d)

"""

"""
from  collections import defaultdict

d = defaultdict(int)

with open("sample.log") as file:
    for line in file:
        if line.strip():
            for letter in line:
                if letter in "aeiouAEIOU":
                    d[letter] += 1

print(d)

"""



#73 Write a program to print all numeric values in a list
items = ['apple', 1.2, 'google', '12.6', 26, '100']

"""
items = ['apple', 1.2, 'google', '12.6', 26, '100']

# for i in items:
#     if isinstance(i,(int,float)):
#         print(i)


for j in items:
    if type(j) in (int,float):
        print(j)
"""


#74 Triangle Patterns

"""
*
* *
* * *
* * * *
* * * * *

"""
"""
for i in range(1,6):
    print(f'{"* " * i:<10}')

    """

#left justified inverted triangle

"""
* * * * *
* * * *
* * *
* *
*
"""


"""for i in range(1,6)[::-1]:
    print(f'{"* " * i:<10}')"""



#right justified triangle
"""
        *
      * *
    * * *
  * * * *
* * * * *

"""

"""
for i in range(1, 6):
    print(f'{"* " * i:>10}')
"""

#right justified inverted triangle

"""

* * * * *
  * * * *
    * * *
      * *
        *
"""

"""
for i in range(1, 6)[::-1]:
    print(f'{"* " * i:>10}')

"""


#center justified

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

"""
for i in range(1, 6):
    print(f'{"* " * i:^10}')
"""



##center justified inverted

"""
* * * * *
 * * * *
  * * *
   * *
    *

for i in range(1, 6)[::-1]:
    print(f'{"* " * i:^10}')
"""


#number left justified

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


pattern = ""

for i in range(1,6):
    pattern = pattern + str(i) + " "
    print(pattern)

"""

#number right justified

"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

pattern = ""
for num in range(1, 6):
	pattern = pattern + str(num) + " "
	print(f'{pattern:>10}')

"""


#center justified

"""
   1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5


pattern = ""
for num in range(1, 6):
	pattern = pattern + str(num) + " "
	print(f'{pattern:^10}')

"""



#75 Write a program count the occurrence of a particular word in the file
"""
def occurrence(pattern):
    with open("sample.log") as file:
        count = 0
        for line in file:
            if line.strip():
                for word in line.split():
                    if word == pattern:
                        count += 1
        print(count)

occurrence("INFO")

"""
"""
def occurrence(pattern):
    with open("sample.log") as file:
        count = 0
        for line in file:
            if line.strip():
                for word in line.split():
                    if word == pattern:
                        count += line.split().count(word)
        print(count)

occurrence("INFO")
"""


#76 Write a program to map a product to a company and build a dictionary with company and list of products pair
"""
all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows','iOS', 'Google Drive', 'One Drive']


apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}


brands = {"apple_products": [], "google_products":[],"msft_products":[]}
no_brand ={"unclassified_brand":[]}

for product in all_products:
    if product in apple_products:
        brands["apple_products"].append(product)
    elif product in google_products:
        brands["google_products"].append(product)
    elif product in msft_products:
        brands["msft_products"].append(product)
    else:
        no_brand["unclassified_brand"].append(product)

print(brands)
print(no_brand)


"""


"""
from collections import defaultdict

d = defaultdict(list)

for product in all_products:
    if product in apple_products:
        d["apple_products"] += [product]

    elif product in google_products:
        d["google_products"] += [product]

    else:
        d["msft_products"] += [product]

print(d)
"""



#77 Write a program to rotate items of the list

names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]


"""

def _rotate(iterable,n):
    for _ in range(n):
        item = iterable.pop()
        iterable.insert(0,item)
    return iterable

print(_rotate(names,2))

"""


"""
def rotate_(lst,n):
        rotated_list = lst[-n:] + lst[:-n]
        return rotated_list

print(rotate_(names,3))
"""

"""
def rotate_(lst,n,direction ="right"):
        if direction == "right":
            rotated_list = lst[-n:] + lst[:-n]
        elif direction == "left":
            rotated_list = lst[n:] + lst[:n]
        else:
            raise ValueError("invalid error")

        return rotated_list

print(rotate_(names,3,direction="left"))

"""


#78 Write a program to rotate characters in a string


"""
def rotate_char(iterable,n):
    rotated = iterable[-n:] + iterable[:-n]
    return rotated

print(rotate_char("Helloworld",3))

"""

#79 Write a program to count the number of white spaces in a given string

sentence = "Hello world welcome to Python Hi How are you. Hi how are you"

#
# no_spaces = findall(r"\s",sentence)
#
# print(len(no_spaces))

"""
def no_spaces(some_string):
    count = 0
    for i in some_string:
        if i == " ":
            count += 1
    print(count)

no_spaces(sentence)

"""



#80 80 Write a program to print only non-repeated characters in a string

st = 'helloworld'
repeate_char = []
non_repeated_char = []

for i in st:
    if i not in non_repeated_char:
        non_repeated_char.append(i)
    else:
        repeate_char.append(i)

# print(non_repeated_char)
# print(repeate_char)




#82 Write a program to print all the consonants in a given string

word = 'helloworld'
consonants = []
for i in word:
    if i not in "aeiouAEIOU":
        consonants.append(i)
#print(consonants)



#83 Write a program to count the number of commented lines in a text file

"""
with open("sample.txt","r") as file:
    commented_lines = 0
    for line in file:
        clean_line = line.strip()
        if clean_line:
            if line.startswith("#"):
                commented_lines += 1
    print(commented_lines)
"""


#84 Write a program to check if the year is leap year or not










#87 Write a program to count no of capital letters in a string
from re import findall

sentence_= "Hi How are You WelCome to PytHon"
no_capital_letters = findall(r"[A-Z]",sentence_)
# print(len(no_capital_letters))
# print(no_capital_letters)


capital_letters = 0
letters = []
for i in sentence_:
    if "A" < i < "Z":
        letters.append(i)
        capital_letters += 1
#
# print(letters)
# print(capital_letters)




#88 Write a program to get the below output
"""
*
* *
*
* * *
*
* * * *
*
* * * * *
"""

"""
for i in range(1,6):
    print("*")
    print(f'{"* " * i:<10}')

"""



#89 Write a program to get the below output
"""
[1, 2]
 [3, 4]
 [5, 6]
 [7, 8]
 [9]
 """
"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0,len(a),2):
   print(a[i:i+2])

"""

#slice it in 3 length words
#dictionary sort in ascending

id = "idfcfirstbank"
f = []

for i in range(len(id)-2):
    f.append(id[i:i+3])
# print(len(f))
# print(f)

d = {tuple(item):item for item in f}
#print(sorted(d.items(),key=lambda value:value ))



#90 Write a program to check if the elements in the second list is series of continuation of the
#items in the first list

a = [10, 12, 14, 16, 18]
b = [20, 22, 24, 26, 28]
"""
#first method
def continuation(list1,list2):
    if len(list1) != len(list2):
        return False

    if len(list1) > 1:
        common_difference = list1[1] - list1[0]
    else:
        common_difference = 0

    for i in range(0,len(list2)):
        if list2[i] + common_difference != list2[i+1]:
            return False
        return True

if continuation(a,b):
    print("second list is continuation of first list ")
else:
    print("nothing")
"""
"""
def continuation_(list1,list2):
    diff = list1[0] - list2[0]

    for l1,l2 in zip(list1,list2):
        if l1-l2 != diff:
            return False
        return True

if continuation_(a,b):
    print("continued list")
else:
    print("nothing")
"""



#92 Write a program to find the first repeating character in a string

s = 'helloworld'

"""
for i in s:
    if s.count(i) > 1:
        print(i)
        break
"""

"""
s1 = ""
for i in s:
    if i not in s1:
        s1 += i
    else:
        print(i)
        break
"""



#93 Write a program to find the index of nth occurrence of a sub-string in a string

sentence = "hello world welcome to python hello hi how are you hello there"
from re import finditer

"""
def find_nth(main_string,subs_tring,occurance):
    result = finditer(subs_tring, main_string)
    count = 0
    for item in result:
        count += 1
        if count == occurance:
            print(item.start())

find_nth(sentence,"hello",1)
"""
"""

def find_nth_occurrence(main_string, sub_string, n):
    start = main_string.find(sub_string)
    while start >= 0 and n > 1:
        start = main_string.find(sub_string, start + len(sub_string))
        n -= 1
    return start

print(find_nth_occurrence(sentence,"hello",1))

"""


#94 Write a program to print prime numbers from 1 to 50

def prime_numbers(number):
    if number > 1:
        for i in range(2,number//2+1):
            if number % i == 0:
                return False
        return True
    return False


#print([num for num in range(1,50) if prime_numbers(num)])





#95 Write a program to sort a list which has mix of both odd and even numbers, the sorted list should have odd numbers first and then even numbers in sorted order
"""
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]

odd = []
even = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

sorted_list = sorted(odd) + sorted(even)
print(sorted_list)

"""


#96 Write a program to sort a list which has mix of both odd and even numbers, in the sorted
#list, odd numbers should be in ascending order and even numbers should be in descending order
"""
a = [3, 4, 1, 7, 2, 12, 8, 6, 9, 11]

odds = sorted([i for i in a if i % 2 == 1])
evens = sorted([i for i in a if i % 2 == 0],reverse=True)
sorted_list = odds + evens
print(sorted_list)
"""



#Bubble sort ####Important#####################################

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(len(my_array)-1):
    flag = False
    for j in range(len(my_array)-1-i):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            flag = True
    if not flag:
        break

#print("Sorted array:", my_array)




#97 Write a program to count the number of occurrences of non-special characters in a given string

s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'

a = findall(r"\w",s)
# print(a)
#print(len(a))


s1 = ""

for i in s:
    if ord(i) in range(ord("a"),ord("z")+1):
        s1 += i
    elif ord(i) in range(ord("A"),ord("Z")+1):
        s1 += i
#print(len(s1))




#98 Grouping Flowers and Animals in the below list
items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']

groups = {}

for item in items:
    l = item.split("-")
    if l[1] not in groups:
        groups[l[1]] = [l[0]]
    else:
        groups[l[1]].append(l[0])

#print(groups)



#99 Grouping files with same extensions
files = ['apple.txt', 'yahoo.pdf', 'gmail.pdf', 'google.txt', 'amazon.pdf', 'facebook.txt','flipkart.pdf']


groups = {}

for file in files:
    l = file.split(".")
    if l[1] not in groups:
        groups[l[1]] = [l[0]]
    else:
        groups[l[1]].append(l[0])

#print(groups)




#100 Filter only those characters except digits

s = '@hello12world34welcome!123'
s1 = ""
#print(findall(r"[^\d]",s))


# for i in s:
#     if ord(i) not in range(ord("0"),ord("9")+1):
#         s1 += i
# #print(s1)

"""
for i in s:
    if not i.isdigit():
        s1 += i
#print(s1)
"""

#101 Count number of words in a sentence. ignore special characters.

sentence = "Hi there! How are you:) How are you doing today!"

#print(len(findall(r"\w+",sentence)))

words = ""

for char in sentence:
    if char.isalpha() or char.isspace():
        words += char

#print(words)





#102 Grouping even and odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

d = {}

for i in numbers:
    if i % 2 == 0:
        if "even" not in d:
            d["even"] = [i]
        else:
            d["even"] += [i]
    else:
        if "odd" not in d:
            d["odd"] = [i]
        else:
            d["odd"] += [i]

#print(d)



#103 Find all max numbers from the below list
"""
numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]

def max_numbers(iterable):
    max_num = iterable[0]
    for i in iterable:
        if i > max_num:
            max_num = i
    return max_num

print(max_numbers(numbers))

for i in numbers:
    if i == max_numbers(numbers):
        print(i)
"""
"""
max_num_ = max(numbers)

for i in numbers:
    if i == max_num_:
        print(i)
"""



#104 Find all max length words from the below sentence

sentence = "hello world hi apple you yahoo to you"
"""
max_length_word = max(sentence.split(),key=len)

for i in sentence.split():
    if len(i) == len(max_length_word):
        print(i)
"""
"""
def max_length(iterable):
    words = iterable.split()
    max_len_word = words[0]
    for i in words:
        if len(max_len_word) == len(i):
            max_len_word = i
    return max_len_word

#print(max_length(sentence))

for i in sentence.split():
    if len(i) == len(max_length(sentence)):
        print(i)

"""




#105 Find the range from the following string

"""
sentence = '0-0,4-8,20-20,43-45'

# Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]
output = []
nums = sentence.split(",")
#print(nums)

for i in nums:
    n1,n2 = i.split("-")
    output += (list(range(int(n1),int(n2)+1)))
#print(output)
"""


#106 Can we override a static method in python?
#ANS -- Yes we can
class Parent:
    @staticmethod
    def demo():
        print('Running demo in Parent')
class Child(Parent):
    @staticmethod
    def demo():
        print('Running demo in Child')
#
# c = Child()
# c.demo()



#107 Write a function which returns the sum of lengths of all the iterables
#total_length([1, 2, 3], (4, 5))


#print(sum([1,2,3,4,5]))


"""
def total_length(*iterables):
    total = []
    for item in iterables:
        total.append(len(item))
    return sum(total)
"""

def total_length(*args):
    count = 0
    for arg in args:
        count += len(arg)
    return count
#
# print(total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart']))
# print(total_length([1, 2, 3], (4, 5),[3,5]))



#108 Replace whitespaces with newline character in the below string
"""
sentence = "Hello world welcome to python"
s = ""
for i in sentence:
    if i.isspace():
        s += "\n"
        #s += i.replace(" ","\n")
    else:
        s += i
#print(s)
"""


#109 Replace all vowels with "*"
"""
sentence = "hello world welcome to python"
s1 = ""
for i in sentence:
    if i in "AEIOUaeiou":
        s1 += "*"
    else:
        s1 += i

print(s1)
"""

# #110 Replace all occurances of "Java" with "Python" in a file
"""
with open("textfile.txt","r") as fr,open("textfile2.txt","w") as fw:
    new_lines = []
    pattern = "java"
    for line in fr:
        if pattern in line:
            new_line = line.replace("java","python")
            new_lines.append(new_line)
    fw.writelines(new_lines)
"""

"""
with open("textfile.txt") as file, open("textfile2.txt", "w") as write_file:
    for line in file:
        n_line = []
        for word in line.split():
            if word == "java":
                n_line.append("python")
            else:
                n_line.append(word)
        line = " ".join(n_line)
        write_file.write(line + "\n")
"""



#111 Maximum sum of 3 numbers and Minimum sum of 3 numbers
numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]

#1st method
"""
print("max_sum:",sum(sorted(numbers)[-3:]))
print("min_sum:",sum(sorted(numbers)[:3]))
"""
#2nd method
m1 = m2 = m3 = -1

"""
for i in range(len(numbers)):
    m1 = numbers.pop(numbers.index(max(numbers)))
    m2 = numbers.pop(numbers.index(max(numbers)))
    m3 = numbers.pop(numbers.index(max(numbers)))
    break
max_sum = m1 + m2 + m3
print(max_sum)

for i in range(len(numbers)):
    m1 = numbers.pop(numbers.index(min(numbers)))
    m2 = numbers.pop(numbers.index(min(numbers)))
    m3 = numbers.pop(numbers.index(min(numbers)))
    break

min_sum = m1 + m2 + m3

print(min_sum)
"""

#3rd method
"""
def find_max_min_sum_of_three(nums):
    if len(nums) < 3:
        return None, None

    # Initialize variables for maximum sum
    max1 = max2 = max3 = float('-inf')


    # Initialize variables for minimum sum
    min1 = min2 = min3 = float('inf')

    # Find maximum sum
    for num in nums:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

    max_sum = max1 + max2 + max3

    # Find minimum sum
    for num in nums:
        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
        elif num < min2:
            min3 = min2
            min2 = num
        elif num < min3:
            min3 = num

    min_sum = min1 + min2 + min3

    return max_sum, min_sum


# Example usage:
nums = [5, 2, 10, 1, 8, 12]
max_sum, min_sum = find_max_min_sum_of_three(numbers)
"""
# print("Original list:", numbers)
# print("Maximum sum of three numbers:", max_sum)
# print("Minimum sum of three numbers:", min_sum)


#112 Write a program to get the output as below
# i/p is "python@#$%pool"
# o/p should be ['PYTHON', 'POOL']

s = "python@#$%pool"
#print([i.upper() for i in findall(r"\w+",s)])
"""
def string_finder(some_string):
    new_string = ""
    for i in some_string:
        if i.isalpha():
            new_string += i.upper()
        else:
            new_string += " "

    return new_string
print(string_finder(s).split())

"""


#114 Write a program to get the indexes of each item in the below list
"""
names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
#output should be - {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}

output = {}
for index, name in enumerate(names):
    if name not in output:
        output[name] = [index]
    else:
        output[name] += [index]
print(output)

"""

#115 Write a program to print "Bangalore" 10 times without using "for" loop
""
#print("Bengaluru\n"* 10)
""

#116 Write a program to print all the words which starts with letter 'h' in the given string

string = 'hello world hi hello universe how are you happy birthday'
#print(findall(r"\bh\w+\b",string))
"""
def h_words(string):
    words = string.split()
    h_words_ = []
    for word in words:
        if word.startswith("h"):
            h_words_.append(word)
    return h_words_
#print(h_words(string))
"""

"""
def h_words__(string):
    if isinstance(string,str):
        words = string.split()
        for word in words:
            if not word.startswith("h"):
                words.remove(word)
        return words

print(h_words__(string))
"""


#117 Write a program to sum all even numbers in the given string

sentence = 'hello 123 world 567 welcome to 9724 python'

#print("sum_even_numbers:",sum([int(i) for i in findall(r"\d",sentence) if int(i) % 2 == 0]))
"""
def even_sum(some_string):
    sum_ = 0
    if isinstance(some_string,str):
        for i in some_string:
            if i.isdigit() and int(i) % 2 == 0:
                sum_ += int(i)
    return sum_

print(even_sum(sentence))
"""


#118 Write a program to add each number in word1 to number in word2


word1 = 'hello 1 2 3 4 5'
word2 = 'world 5 6 7 8 9'

# word1_ = [int(i)for i in findall(r"\d",word1)]
# word2_ = [int(i)for i in findall(r"\d",word2)]
# for i,j in zip(word1_,word2_):
#     print(i+j,end=",")
"""
print()

for i,j in zip(word1,word2):
    if i.isdigit() and j.isdigit():
        print(int(i)+int(j),end=",")
"""


#119 Write a program to filter out even and odd numbers in the given string
sentence = 'hello 123 world 456 welcome to python498675634'

"""
def filter_number(variable):
    evens = []
    odds = []
    for i in variable:
        if i.isdigit() and int(i) % 2 == 0:
            evens.append(int(i))
        elif i.isdigit() and int(i) % 2 != 0:
            odds.append(int(i))
    return (evens,odds)

print(filter_number(sentence))
"""
"""
def filter_number(variable):
    evens = list(filter(lambda item: int(item) % 2 == 0, [int(i) for i in variable if i.isdigit()]))
    odds = list(filter(lambda item: int(item) % 2 != 0, [int(i) for i in variable if i.isdigit()]))
    return (evens,odds)

print(filter_number(sentence))
"""
# evens = [int(i) for i in findall(r"\d",sentence) if int(i) % 2 == 0]
# odds = [int(i) for i in findall(r"\d",sentence) if int(i) % 2 != 0]
#
# print(evens)
# print(odds)

# even_numbers = list(filter(lambda item:int(item) % 2 == 0,[int(i) for i in findall(r"\d",sentence)]))
# print(even_numbers)
"""
evens = list(filter(lambda item:int(item) % 2 == 0,[int(i) for i in sentence if i.isdigit()]))
print(evens)
odds = list(filter(lambda item:int(item) % 2 != 0,[int(i) for i in sentence if i.isdigit()]))
print(odds)
"""



#120 Write a program to print all the number which are starting with 8
"""
numbers = ['857', '987', '8', '120', '888888', '547', '7674', '89', '589', '388888', '2889']

nums_8 = [int(num) for num in numbers if num.startswith("8")]
print(nums_8)

f_numbers =[int(i) for i in list(filter(lambda item:item[0] == "8",numbers))]
print(f_numbers)
"""


#121 Write a program to remove duplicates from the list without using set or empty list
l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]
"""
i = 0
while i < len(l1):
    while l1[i] in l1[i+1:]:
        l1.remove(l1[i])
    i += 1
print(l1)
"""

"""
l2 = l1.copy()
for i in l2:
    if l1.count(i) > 1:
        l1.remove(i)
print(l1)
"""


#122 Print all the missing numbers from 1 to 10 in the below list
"""
numbers1 = [1, 3, 6, 8, 10]
missing_numbers = []
for i in range(1,11):
    if i not in numbers1:
        missing_numbers.append(i)
print(missing_numbers)
"""

#123 Write a python program to get the below output
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
# o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
opt = []
"""
for i in range(len(list1)):
    for j in range(len(list2)):
        opt.append(f"{list1[i]}{list2[j]}")
print(opt)
"""

"""
for i in list1:
    for j in list2:
        opt.append(str(i)+j)
print(opt)
"""


#124 Write a python program to get the below output
word = "AAAAaaccYYY"
# o/p ['Y3', 'c2', 'a2', 'A4']

d = {}
"""
for i in word:
    count = 0
    if i not in d:
        for j in word:
            if j == i:
                count += 1
        d[i] = count
"""
# print("".join([i+str(j) for i,j in d.items()]))
# print([i+str(j) for i,j in d.items()])
"""
for i in word:
    d[i] = d.get(i,0) + 1
print([i+str(j) for i, j in d.items()])
"""

"""
for i in word:
    d[i] = word.count(i)
print([i+str(j) for i, j in d.items()])
"""



#125 What is the output of the below function call

class Demo:
    def greet(self):
        print("hello world")

    def greet(self):
        print("hello universe")

#output == takes latest implementaion



#126 In the list below, find all the number pairs which results in 10 either when added or subtracted
a = [3, 5, -4, 8, 11, 1, -1, 6]
"""
pairs = []
for x, y in combinations(a,2):
    if x + y == 10 or abs(x - y )== 10:
        pairs.append((x,y))
print(pairs)
"""

"""
pairs = []
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] + a[j] == 10 or abs(a[i] - a[j]) == 10:
            pairs.append((a[i],a[j]))
print(pairs)
"""


#127 Write a decorator to prefix +91 to the original phone numbers
"""
numbers2 = [1234567890, 123456790, 1234567890]
numbers2 = ["+91" + str(i) for i in numbers2]
print(numbers2)
"""
"""
numbers2 = [1234567890, 123456790, 1234567890]
def prefix_number(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return ["+91" + str(i) for i in result]
    return wrapper

@prefix_number
def number_p(iterable):
    return iterable

print(number_p(numbers2))

"""


#128 Write a program to get the below output
"""
d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# o/p should be ['b', 'd']

filtered_keys = [i for i,j in d.items() if j % 2 == 0]
print(filtered_keys)
"""


#132 Reverse a list without using any built-in functions and slicing
a = [1, 2, 3, 4, 5]
# a.sort(reverse=True)
# print(a)
# print(sorted(a,reverse=True))
"""
for i in range(len(a)):
    flag = False
    for j in range(len(a)-1-i):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    if flag:
        break
print(a)
"""


#133 Write a program to get the below output
# i/p = "10.20.30.40"
# o/p = "40.30.20.10"
"""
p = "10.20.30.40"
f = ".".join(p.split(".")[::-1])
print(f)
"""

"""
p = "10.20.30.40"
parts = p.split(".")
reversed_parts = [i for i in parts[::-1]]
print(reversed_parts)
"""

"""
reversed_parts = []
while len(parts) > 0:
    reversed_parts.append(parts.pop())
print(reversed_parts)
"""

#138 What is the output of the below program.

# print([1, 2, 3, 4] * 2)


#143 write a program to get the below output using while loop

"""
1
12
123
1234
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
"""

"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
"""
for i in range(1,5)[::-1]:
    for j in range(1,i+1):
        print(j,end=' ')
    print()
"""


#144 write a program to get the below output

items = ['$123.45', '$434.23', '$567.89']
# o/p [123.45, 434.23, 567.89]

# print([float(i[1:]) for i in items])



#145 Generator function for Fibonacci series program
"""
def fibonacci_generator(num, a=0,b=1):
    if num <= 0:
        return 0
    elif num <= 1:
        return 1
    else:
        while True:
            yield a
            a,b = b,a+b


result = fibonacci_generator(6)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# print(next(result))
"""




# nth fibonacci number

"""
def fib_number(num):
    if num <= 0:
        return 0
    elif num <= 1:
        return 1
    else:
        a,b = 0,1
        for _ in range(2,num+1):
            a,b = b,a+b
        return b
print(fib_number(6))
"""














#find the first and last index of the target

def find_first_last_indices(arr, target):
    first_index = last_index = -1
    # Find first occurrence
    for i in range(len(arr)):
        if arr[i] == target:
            first_index = i
            break

    # Find last occurrence
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == target:
            last_index = i
            break

    return (first_index, last_index)

# Example usage:
l = [1, 3, 5, 8, 8, 8, 8, 8, 8, 8, 8, 9]
target = 8
first, last = find_first_last_indices(l, target)
# print(f"First index of {target}: {first}")
# print(f"Last index of {target}: {last}")


#finding the nth occurance of a number

some_list = [1,3,5,8,8,8,8,8,8,8,8, 9]

def find_nth_occurrence(nums, target, n):
    count = 0
    for index,num in enumerate(nums):
        if num == target:
            count += 1
            if count == n:
                return index
    return -1

# print(find_nth_occurrence(some_list,8,1))
# print(find_nth_occurrence(some_list,2,5))

##############Binary Sort########################

#program to find the index of the given value
def binarySearch(arr, targetVal):

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid

        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

#print(binarySearch(myArray,9))



######################################linear Search####################

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

arr = [3, 7, 2, 9, 5]
targetVal = 9
#print(linearSearch(arr, targetVal))


















#

# class A:
#     def sampale(self):
#         print("some text")
#
# class B(A):
#     def sampale(self, a=0,b=0):
#         if a!=0 and  b!=0:
#             print(f"next text {a} and {b} ")
#         elif a!=0 :
#             print(f"next text  {a} ")
#         elif b!=0:
#             print(f"next text  {b} ")
#
# b = B()
# b.sampale(b=6)




"""
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

driver = WebDriver()
driver.get("https://www.amazon.in/")
driver.maximize_window()

search_box = driver.find_element("id","twotabsearchtextbox")
search_box.send_keys("iphone")
search_button = driver.find_element("id","nav-search-submit-button")
search_button.click()
sleep(5)

iphones = driver.find_elements("xpath",'//span[@class="a-size-medium a-color-base a-text-normal"]')

iphones_list = [iphone.text for iphone in iphones]

print(iphones_list)
"""




"""
s = "I am from Bengaluru"
#o/p = Bengaluru am From I

t = (s.split())
t1 = []
last = t.pop()
first = t.pop(0)
t.insert(0,last)
t.append(first)
print(" ".join(t))
"""

"""
#remove duplicates

a = [2,4,5,5,4,6,9]
#type casting
print(set(a))

#1st method
a1 = []

for i in a:
    if i not in a1:
        a1.append(i)
print(a1)

#2nd method
for i in a:
    if a.count(i) > 1:
        a.remove(i)
print(a)

"""































































# students = [
#     {"name": "Alice", "age": 20, "major": "Physics"},
#     {"name": "Bob", "age": 21, "major": "Mathematics"},
#     {"name": "Charlie", "age": 22, "major": "Biology"}
# ]
#
#
# # def get_age(item):
# #     return item["major"]
# #
# # sort_major = sorted(students,key=get_age)
# # print(sort_major)
#
# t = sorted(students,key=lambda student:student["major"],reverse=True)
#
# print(t)
###########################################################################################################

#####regular expression###########



#from re import findall

# pattern = findall("hello","hello how  are you ganesh hello")
# print(pattern)

# pattern = findall("sep[ea]rated","the [age is seperated from the book separated")
#
# print(pattern)


# pattern = findall("[aeiou]","hello dash how are you")
# print(len(pattern))

# P = findall("[abcd]","hi ganesh how are you")
# print(P)
#


# number = findall("[1234567890]", "the cost of the computer RS.2563 ")
# number1 = findall("[0-9]", "the cost of the computer RS.2563 ")
# print(number1)


# heading = "<h1>ganesh testyantra</h1>, <h6>ganesh testyantra</h6> <h3>ganesh testyantra</h3>"
# p = findall(r"<h[0-9]>",heading)
# print(p)

#
# st = "546 python 532 programming 6545 languge  66 dfhf 523 65"
#
# p = findall(r"[^\w]",st)
# print(len(p))


# sentence = "     thi sis a sentence        "
#
# p = findall(r"\s", sentence)
#
# leading_spaces = findall(r"^\s+",sentence)
# trailing_spaces = findall(r"\s+$",sentence)
#
# print(len(leading_spaces[0]))
# print(len(trailing_spaces[0]))

# mobile_no = "+91 22 1234 5678 bhdsdhas nudhsad hdjasdj +91 98 1234 5658"
#
# m = findall(r"\+91.\d{2}.\d{4}.\d{4}",mobile_no)
#
# print(m)
# #
# w = "hello how are you  what is your name"
#
# p = findall(r"\b\w{3}\b",w)
#
# print(p)













""""
from selenium.webdriver.chrome.webdriver import WebDriver

driver = WebDriver()

driver.get("https://www.demoblaze.com/")
driver.maximize_window()

#p_names = driver.find_elements("xpath",'//a[@class="hrefch"]')
sleep(3)
p_names = driver.find_elements("class name","card-block")
d={}
for i in p_names:
    d[i.find_element("class name","card-title").text] = i.find_element("tag name","h5").text
print(d)
"""





































