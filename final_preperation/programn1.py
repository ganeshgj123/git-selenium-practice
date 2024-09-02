# temperatures = {"bangalore": (26, 29), "chennai": (29, 33), "delhi": (28, 35)}
# for value1,value2 in temperatures.values():
#     print(value1,value2)
#


# location = {'country': 'India', 'states': ['Karnataka', 'Andra', 'Kerala']}
# print(location["states"][2])

prices = {'IBM': {'current': 90.1, 'low': 88.3, 'high': 92.7}, 'HP': {"current": 29.70, "low": 28.30, "high": 31.2}}

# print(prices['IBM']['current'])

# for i in prices['IBM'].items():
#     print(i)

# print(prices.get("IBM"))


# Counting number of characters in a string
"""
word = 'abracadabraca'
d = {}
for i in word:
    if i not in d:
        d[i] = word.count(i)
print(d)

"""

"""
word = 'abracadabraca'
d = {}
for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
"""

"""
word = 'abracadabraca'
d = {}
for i in word:
    if i not in d:
        count = 0
        for j in word:
            if i == j:
                count += 1
        if count > 1:
            d[i] = count
print(d)
"""

"""
word = 'abracadabraca'
d = {}
for i in word:
    if i not in d:
        count = 0
        for j in word:
            if i == j:
                count += 1
        d[i] = count
print(d)
"""

"""
word = 'abracadabraca'
d = {}
for i in word:
    d[i] = d.get(i,0) + 1
print(d)
"""

"""
word = 'abracadabraca'
d = {}
d = d.fromkeys(word,0)
print(d)
for i in word:
    d[i] = d[i] + 1
print(d)
"""

# Counting number of vowels in a string
"""
sentence = 'hello world welcome to python'
d = {}

d = d.fromkeys(sentence,0)
for i in sentence:
    if i in "aeiouAEIOU":
        d[i] = d[i] + 1

print(d)
"""
"""
sentence = 'hello world welcome to python'
d = {}
for i in sentence:
    if i in "aeiouAEIOU":
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
print(d)
"""
"""
sentence = 'hello world welcome to python'
d = {}
for i in sentence:
    if i in "aeiouAEIOU":
        if i not in d:
            d[i] = sentence.count(i)
print(d)
"""
"""
sentence = 'hello world welcome to python'
d = {}
for i in sentence:
    if i in "aeiouAEIOU":
        d[i] = d.get(i,0) + 1
print(d)
"""

# Counting occurances of word in the string (using defaultdict)
sentence = "hello world welcome to python hello hi hello hello"
words = sentence.split()
# print(words)
"""
from collections import defaultdict
d = defaultdict(int)
for i in words:
    d[i] += 1
print(dict(d))
"""

"""
d = {}
for i in words:
    d[i] = d.get(i,0) + 1
print(d)
"""

"""
d = {}
for i in words:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
"""

"""
d = {}
for i in words:
    if i not in d:
        count = 0
        for j in words:
            if j == i:
                count += 1
        d[i] = count
print(d)
"""

"""
d = {}
d = d.fromkeys(words,0)
for i in words:
    d[i] = d[i] + 1
print(d)
"""

# Counting occurances of each character in the string (using defaultdict)
"""
s = 'abracadabraca'
from collections import defaultdict
d = defaultdict(int)
for i in words:
    d[i] += 1

print(dict(d))
"""



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
"""
from collections import defaultdict

s = defaultdict(list)
for i,j in cities:
    s[i].append(j)
print(dict(s))

"""

"""
d = {}
for i, j in cities:
    if i not in d:
        d[i] = [j]
    else:
        d[i].append(j)
print(d)
"""

"""
d = {}
for i,j in cities:
    d[i] = d.get(i,[]) + [j]
print(d)
"""



#################################lists#######################

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

# names.extend(('netflix', 'walmart', 'kroger'))
# print(sorted(set(names)))
# names.sort()
# print(names)

from copy import copy,deepcopy

####### shallow copy

# original = [[1, 2, 3], [4, 5, 6]]
# s = copy(original)
# original[0][1] = 100
# print(original)
# print(s)
#


# a = [(1,2,3,6,5,4,7,9),{23:1,56:2,58:3}]
# t = copy(a)
# a[1][56]= 100
# print(a)
# print(t)



############# deep copy

"""
original = [[1, 2, 3], [4, 5, 6]]
d = deepcopy(original)
original[0][1] = 100
d[1][1] = 200
print(original)
print(d)
"""


######################################### unpacking ############################################################

"""
data = ['IBM', 50, 91.1, (2019, 7, 17)]
a,b,c,d = data
d1,d2,d3 = d
# print(d1)
# print(d2)
# print(d3)

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minimum,*rest,maximum = data1
print(rest)
print(maximum)
print(minimum)
"""

"""
count = 1
sum_ = 0
while count <= 5:
    sum_ += count
    count += 1
print(sum_)
"""
sentence = 'hello 123 world 456 welcome to python498675634'

"""
def char_count(string,char,count = 0,index = 0):
    while index < len(string):
        if string[index] == char:
            count += 1
        index += 1
    return (char,count)

print(char_count(sentence,"h"))
"""


# d = {}
# for i in sentence:
#     if i not in d:
#         count = 0
#         for j in sentence:
#             if j == i:
#                 count += 1
#         d[i] = count
# print(d)





def prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num % i == 0:
            return False
    return True

# print(prime(23))

series = []
for i in range(1,50):
    if prime(i):
        series.append(i)
print(series)



"""
def generate_prime_series(num=0):
    while True:
        if is_prime(num):
            yield num
        num += 1


prime_series = generate_prime_series()
print(next(prime_series))
print(next(prime_series))
print(next(prime_series))
print(next(prime_series))
"""


"""
@pytest.mark.create_firmware
def test_create_firmware():
    response = Firmware().create_firmware()
    response_data = response.json()
    assert response.status_code == 200
    str_response = response.text
    r = loads(str_response)
    assert r["message"] == "success"
"""





