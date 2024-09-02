#1. Write a program to find the length of the string without using inbuilt function (len)

s = "without"

count = 0
for _ in s:
    count += 1
#print(count)


#2. Write a program to reverse a string without using any inbuilt functions.

a = "reverse"

#print(a[::-1])

rev_string = ""
for i in a:
    rev_string = i + rev_string
#print(rev_string)



#3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".

t = "Hello World"
str_replace = t.replace("World","Universe")
#print(str_replace)

l = t.split()
l[1] = "Universe"
#print(" ".join(l))


#4. How to convert a string to a list and vice-versa.

s = "another"

# print(list(s))
# print("".join(list(s)))


#5. Covert the string "Hello welcome to Python" to a comma separated string.
t = "Hello welcome to Python"

# print(t.replace(" ",","))
# print(",".join(t.split()))


#6. Write a program to print alternate characters in a string.

#print("alternate"[1::2])


#7. Write a Program to print ascii values of the characters present in a string.

w = "Python"
#print([ord(i) for i in w])



#8. Write program to convert upper case to lower case and vice-versa without using inbuilt method.

d = "Hello World"

g = ""

for char in d:
    if "a" < char < "z":
    #if ord(char) in range(ord("a"),ord("z")+1):
        char = ord(char) - 32
        g += chr(char)

    elif "A" < char < "Z":
    #elif ord(char) in range(ord("A"),ord("Z")+1):
        char = ord(char) + 32
        g += chr(char)

#print(g)



#9. Write program to swap two numbers without using 3rd variable

# a,b = 2,3
# print(a)
# print(b)
#
# a,b = b,a
#
# print(a)
# print(b)


#10. Write program to merge two different lists.
l1 = [1,2,3,4,5]
l2 = [6,7,8,9]
# print(l1+l2)
# l1.extend(l2)
# print(l1)
#


#11. Write program to read a random line in a file. (ex. 50, 65, 78th line)

def random_line(lineno_):
    with open("data.txt") as file:
        for lineno, line in enumerate(file,start=1):
            if lineno == lineno_:
                print(line)
#random_line(5)



#12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)

def random_lines(line1,line2):
    with open("data.txt") as file:
        for lineno, line in enumerate(file,start=1):
            if lineno in range(line1,line2+1):
                print(line)

#random_lines(10,15)



#13 Program to print last "N" lines of a file.

# with open("data.txt") as file:
#     count = 0
#     for i,j in enumerate(file):
#         count += 1
#     print(count)


def last_N_lines(n):
    with open("data.txt") as file:
        for lineno,line in enumerate(file,start=1):
            if lineno in range(n,-1):
                print(line)
# last_N_lines(95)




#check the first number is even or odd

#
# d = 7652342
#
# while d > 10:
#     d = d//10
#     # print(d)
# print(f"{d} is {d % 2 == 0}")




rev = 0
num = 3246
while num > 0:
    rem = num % 10
    rev = rev*10 + rem
    num = num // 10

# print(rev)

rev = ""
s = "12345"
for i in s:
    rev = i + rev
# print(rev)



#find the number of occurences of numbers appearing for the m and n number of times
"""
l = [2,3,2,1,2,3,1,4,5,10,2]

def getOccurenceCount(iterable):
    d = {}
    for i in iterable:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    result = {}
    for j,k in d.items():
        if k not in result:
            result[k] = [j]
        else:
            result[k].append(j)
    return result


print(getOccurenceCount(l))

"""







































