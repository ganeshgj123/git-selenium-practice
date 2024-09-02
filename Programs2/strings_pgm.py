#Reverse words in a given string

"""def rev(str):
    words= str.split()
    l=[]
    for i in words[::-1]:
        l.append(i[::-1])
    print(" ".join(l))

rev("Hello welcome to python")"""




#Encrypt A String To Generate A Password
"""
import string
import random

total = string.ascii_letters + string.digits + string.punctuation
print("".join(random.sample(total, 16)))"""



#Encrypt A Secret Message
"""alphabet = 'abcdefghijklmnopqrstuvwxyz'
Key=3
newMessage = ' '

message = input('Please enter a message: ')
for character in message:
    position = alphabet.find(character)
    newPosition = (position+ Key) % 26
    newCharacter = alphabet[newPosition]
    newMessage += newCharacter

print(newMessage)
"""

#acronym generator

"""t = input("enter the string: ")
words = t.split()
t=""
for i in words:
    t=t+i[0].upper()
print(t)"""


#Count The Number Of Vowels In A String


"""def vowels(str):
    t = 0
    for i in str:
        if i in "AEIOUaeiou":
            t+=1
    print(t)

vowels("please")"""

#Define a function that tests if a string has a letter or number
"""def chkStr(string):
  chk1 = False
  chk2 = False

  for i in string:

#check if the string has a letter
    if i.isalpha():
      chk1 = True

#check if the string has a digit
    if i.isdigit():
      chk2 = True

  return chk1 and chk2

print(chkStr('thisisastring123'))
print(chkStr('thisisalsoastring'))
"""


#Return A List Of Strings From a Multiline String

string3 = '''
100 Projects For Beginners Using Python,
Predict Rocket Launch Delays With Machine Learning And Python,
Creating A WordCloud Using Python,
Automate Text Messages Using Python,
The Beginners Guide To Extracting COBie Data — Part 1'''

#use splitlines() to assign each line as a value in a list

"""z = string3.splitlines()
print(string3,end='\n')
"""


#program to find the number of vowels, consonents, digits and white space characters in a string.
"""
t = "This is umbrella 122343"
print(len(t))
c=0
c1=0
c2=0
c3=0
for i in t:
    if i.isdigit():
        c+=1
    elif i.isspace():
        c1+=1
    elif i in "aeiouAEIOU":
        c2+=1

    elif i not in "aeiouAEIOU":
        c3+=1

print(f"digits{c}")
print(f"spaces:{c1}")
print(f"vowels:{c2}")
print(f"consonants:{c3}")"""

# program to make a new string with all the consonents deleted from the string "Hello, have a good day".
"""
s= "Hello, have a good day"
str=""

for i in s:
    if i in "aeiouAEIOU":
        str+=i
print(str)"""


#find out the largest and smallest word in the string "This is an umbrella".
a = "This an a umbrella jsfskdfksdfds"
"""a = a.split()
minn = a[0]
min_len = len(a[0])
print(min_len)
for i in a:
  if len(i)<min_len:
    min_len = len(i)
    minn = i
print (minn)"""

"""a = "This is an umbrella"
a = a.split()
maxx = a[0]
max_len = len(a[0])
for i in a:
  if len(i)>max_len:
    max_len = len(i)
    maxx = i
print (maxx)
"""

"""l= ["ramesh","suresh","mahesh","gyanesh"]
l.sort()
print(l)"""



#program to make a new string with the word "the" deleted in the sentence "This is the lion in the cage".
"""l="This is the lion in the cage"
words= l.split()
for i in words:
  if i == "the":
    del (words[words.index(i)])
print(words)"""


#anagram
"""print(sorted("listen")==sorted("silent"))"""


#Converting a List into a String
"""lst = ["P", "Y", "T", "H", "O", "N"]
print("".join(lst))"""


#Counting Special Characters in a String
"""import string
s= "re.sub('[w]+', '', spChar)"
c=0
result = string.punctuation

for i in s:
    if i in result:
        c+=1
print(c)"""


#Python program to remove character from string

"""str = "Python"
print(str.replace("t",""))"""


#Python Program to count occurrence of characters in string

"""str="programming"
print(str.count("m"))"""

####OR####
"""count= 0
for i in str:
    if i=="m":
        count+=1
print(count)"""


#Python program in to check string is anagrams or not

"""t1 = list("listen")
t2 = list("silent")
t1.sort()
t2.sort()
print(t1==t2)"""

#######OR####

"""print(sorted("listen") == sorted("silent"))"""


#Program to replace the string space with any given character

s = "character"
"""t= s.replace("c","f")
print(t)
"""
####OR########

"""result= ''
for i in s:
    if i == 'c':
        i = "f"
    result += i
print(result)
"""




#################################################################################################


#Title Case Conversion

"""
"""
def to_title_case(word: str) -> str:
    """
    Converts a string to capitalized case, preserving the input as is

    >>> to_title_case("Aakash")
    'Aakash'

    >>> to_title_case("aakash")
    'Aakash'

    >>> to_title_case("AAKASH")
    'Aakash'

    >>> to_title_case("aAkAsH")
    'Aakash'
    """

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
    """
    Converts a string to title case, preserving the input as is

    >>> sentence_to_title_case("Aakash Giri")
    'Aakash Giri'

    >>> sentence_to_title_case("aakash giri")
    'Aakash Giri'

    >>> sentence_to_title_case("AAKASH GIRI")
    'Aakash Giri'

    >>> sentence_to_title_case("aAkAsH gIrI")
    'Aakash Giri'
    """

    return " ".join(to_title_case(word) for word in input_str.split())


if __name__ == "__main__":
    from doctest import testmod

    testmod()

"""
"""

#######################################################################################################

# wave of a given string

"""
"""
def wave(txt: str) -> list:
    """
    Returns a so called 'wave' of a given string
    >>> wave('cat')
    ['Cat', 'cAt', 'caT']
    >>> wave('one')
    ['One', 'oNe', 'onE']
    >>> wave('book')
    ['Book', 'bOok', 'boOk', 'booK']
    """

    return [
        txt[:a] + txt[a].upper() + txt[a + 1 :]
        for a in range(len(txt))
        if txt[a].isalpha()
    ]


if __name__ == "__main__":
    __import__("doctest").testmod()

"""
"""





















