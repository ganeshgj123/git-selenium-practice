def even():
    num = 0
    while True:
        if num % 2 != 0:
             yield num
        num += 1


result = even()

#
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))


names = ["steve", "John", "alex", "lara", "eve"]

def vowel_names():
    for name in names:
        if name[0] in "AEIOUaeiou":
            yield name

result_ = vowel_names()
# print(next(result_))
# print(next(result_))

"""for i in result_:
    print(i)
"""
vowel_names_ = [name for name in names if name[0] in "AEIOUaeiou"]
# print(vowel_names_)



# yield only the words which have even length


sentence = "python is a programming language"


def even_length():
    for word in sentence.split():
        if len(word) % 2 == 0:
            yield word

# for word_ in even_length():
#     print(word_)

even_length_ = (i for i in sentence.split() if len(i) % 2 == 0 )
# print(list(even_length_))




# generator function to countdown from a number to 0

"""
def countdown_generator(num):
    for i in range(num, -1 , -1):
        yield i

for count in countdown_generator(10):
    print(count)

"""


# generator to yield tuple of name and length pairs

names = ["steve", "John", "alex", "lara", "eve"]

"""def name_length():
    for name in names:
        yield (name,len(name))
        
for i in  name_length():
    print(i)"""


# generator to yield reversed names if the name is of odd length
"""def odd_length():
    for name in names:
        if len(name) % 2 != 0:
            yield (name)

for i in odd_length():
    print(i[::-1])

"""



# yield name as it is if it is a palindrome else reverse it


def pal_name(name):

    if name[::-1] == name:
        yield name
    else:
        yield name[::-1]



# for i in  pal_name("level"):
#     print(i)






##############################################################################################


#Recursion


import sys

sys.setrecursionlimit(2000)

#print(sys.getrecursionlimit())

count = 0
def func():

    global count
    count += 1

    #print("hello",count)
    func()

# func()











from  collections import Counter, defaultdict

with open(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\access-log.txt") as file:

    d = {}
    for line in file:
        if line.strip():
            ip_address = line.split()[0]
            if ip_address not in d:
                d[ip_address] = 1
            else:
                d[ip_address] += 1

#print(Counter(d).most_common(1))


####################################################################################################################


# find the length of each line in the file

#
# with open(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\access-log.txt") as file:
#
#     for line in file:
#         if line.strip():
#             print(len(line))

# find the number of words in each line

# with open(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\access-log.txt") as file:
#
#     for line in file:
#         if line.strip():
#             data = line.split()
#             for words in data:
#                 print(len(d ata))








# count the number of spaces present in the file

#
# with open(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\access-log.txt") as file:
#
#     count = 0
#
#     for line in file:
#         if line.strip():
#             for char in line:
#                 if char == " ":
#                     count += 1
#     print(count)



# with open(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\access-log.txt") as file:
#
#     space = 0
#
#     for line in file:
#
#         data = line.count(" ")
#
#         space += data
#
#     print(space)




#
# with open(r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\access-log.txt") as file:
#     for lineno, line in enumerate(file,1):
#         if lineno == 4 :
#             print(line)
#             break

























# group the players based on their positions
#
# football_file = r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\football.txt"
#
# with open(football_file, encoding="utf-8") as file:
#
#    d = defaultdict(list)
#    header = next(file)
#
#    for line in file:
#
#             player_details = line.split("\t")
#
#             for position in player_details:
#                 if position == player_details[4]:
#                     d[position].append(player_details[-2])
#






   # for i, j in d.items():
   #     print(i,j)


"""alternative"""
#
# football_file = r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\football.txt"
#
# with open(football_file, encoding="UTF-8") as file:
#
#     header = next(file)
#     d_ = defaultdict(list)
#
#     for line in file:
#         position, players = line.split("\t")[4], line.split("\t")[-2]
#         d_[position] += [players]
#
#     for i, j in d_.items():
#         print(i, j)












# group the colors based on the brands

#
# brands_file = r"C:\Users\GANESH S JOSHI\PycharmProjects\SeleniumPython\pythonProject1\Programs2\data.txt"
#
# with open(brands_file, encoding="UTF-8") as file:
#
#    d = defaultdict(list)
#
#
#    for line in file:
#        brand_list = line.split("\t")
#        for brand in brand_list:
#            if brand == brand_list[0]:
#                d[brand].append(brand_list[1])
#
# #
# # for i,j in d.items():
# #     print(i,j)
#







# copy the contents of sample.txt to another file
"""
with open("sample.txt","r") as file :

    data = file.read()


with open("sample2.txt","w") as file:
    data_ = file.write(data)

"""


all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows','iOS', 'Google Drive', 'One Drive']


apple_products = {'iPhone', 'Mac', 'iWatch'}
google_products = {'Gmail', 'Maps', 'Google Drive'}
msft_products = {'Windows', 'One Drive'}

d= defaultdict(list)

"""for product in all_products:
    if product in apple_products:
        d["apple_products"] +=[product]
    elif product in google_products:
        d["google_products"] += [product]
    elif product in msft_products:
        d["msft_products"] += [product]
"""
# for i, j in d.items():
#     print(i,j)

for product in all_products:
    if product in apple_products:
        d[frozenset(apple_products)] +=[product]
    elif product in google_products:
        d[frozenset(google_products)] += [product]
    elif product in msft_products:
        d[frozenset(msft_products)] += [product]

# for i, j in d.items():
#         print(i,j)


#Write a program to replace value present in nested dictionary.

"""d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# Replace "nose" with "net"

# d["b"]["n"] = "net"
# print(d)
l = []
for i in d.items():
     if isinstance(i[1],dict):
         for j in i[1].items():
            print(j.)

"""






































































# with open("sample.txt") as file1, open("abc2.txt","w") as file2:
#
#     for data in file1:
#         copy_data = file2.write(data)


import csv

# with open("employees.csv") as file:
#     obj = csv.DictReader(file)
#
#     for name in obj:
#         print(name["name"])
#

"""
with open("employees.csv") as file:
    obj = csv.DictReader(file)
    d= defaultdict(list)
    for row in obj:
        for item1,item2 in row.items():
            d[item1].append(item2)
    # print(d)

    for i,j in d.items():
        print(i,j)"""













































