
###Tupels#####
#1.write a program to get 1234

t = ('1', '2', '3', '4')

"""d = ""
for i in t:
    d += i
print(d)
"""
#print("".join(t))


#2.Write a program to update the tuple

"""t1 = (1, 2, 3, 4)
t2 = (100, 200, 300)

print(t1+t2)

print(dir(t1))
"""

#3.	How to create a tuple using range function

#print(tuple(range(5)))


################################################################################################################################
#dictionary

#1.	Write a program to get the below output

# sentence = "hello world welcome to python programming hi there"
#
# d = {}
#
# words = sentence.split()

"""for word in words:
    if word[0] not in d:
        d[word[0]] = [word]
    else:
        d[word[0]].append(word)

print(d)
"""


#3.Reverse the values in the dictionary if the value is of type String
"""d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

for key,value in d.items():
    if isinstance(value,str):
        d[key] = value[::-1]
print(d)

"""


#3.	Program to print the number of occurrences of characters in a String without using inbuilt functions.
#s = 'helloworld'


# d = {}
#
# for letter in s:
#    if letter not in d:
#        d[letter] = 1
#    else:
#        d[letter] += 1
# print(d)

"""d = {}

for letter in s:
  d[letter] = s.count(letter)

print(d)  
"""


"""from  collections import defaultdict

d = defaultdict(int)
for letter in s:
        d[letter] += 1
print(d)
"""

#4.Program to print only the repeated characters and count of the same.

s = 'helloworld'

d = {}

"""for letter in s:
    if s.count(letter) > 1:
        d[letter] = s.count(letter)
print(d)
"""

counter = 0

for letter in s:
    if letter not in d:

        d[letter] = counter
print(d)


