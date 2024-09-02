# PYTHON LISTS
"""
0. Objects that hold reference to the other objects are called containers
1. Lists are Mutable
2. Elements in the Lists are Ordered
3. Lists can hold duplicate elements
4. Lists can be indexed by integers starting zero
5. Lists are heterogeneous in nature. (They can point to any kind of objects)
"""

# Creating an List
my_list = []
my_list = [1, 2, 3, 4, 5]
my_list = list()    # Using list constructor
my_list = list('helloworld')
my_list = list([1, 2, 3, 4, 5])

names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']

print(names)    # Prints the items of the List
print(len(names))       # Prints the Length of the List. Index starts from Zero.
print(names[0])     # Prints the item present in the 0th index of the List.


# Adding elements to the List
names.append('gmail')   # Adding element to the list
names.insert(3, 'watsapp')      # Inserts the item at 3rd index.

# Extends the exisitng list with the items of the new list
names.extend(['netflix', 'walmart', 'kroger'])

a = ["apple", "google", "yahoo"]
b = ["gmail", "flipkart", "facebook"]
# Merging two different lists
c = a + b
c = [*a, *b]

print('gmail' in names)     # Prints True if the item is present in the list

# Removing Items from the List
names.remove('kroger')  # Removes the item 'kroger' from the List
names.pop()     # By default this will remove the last item in the List
# pop method returns the item that it has removed from the List
names.pop(3)    # Removes the item in the 3rd index of the List

del names[0]    # Deletes 0th item in the list
# del names[3:6]  # Deletes 3rd, 4th and 5th items in the list
# del names[::2]  # Deletes alternate items in the list
# del names   # Deletes the reference to the list "names"
# del names       # Deletes the entire list

# Making copy of the list (Shallow Copy!!!)
a = [1, 2, 3, 4, 5]
b = a.copy()
  # OR
b = a[:]

# 6_Sorting List's
names.sort()    # Sorts the List in Alphabetical Order
# sort method modifies the list inplace.
names.sort(reverse=True)    # Sorts the List in Decending Order

sorted(names)   # Sorts the List in Alphabetical Order and returns a new list.
# sorted method does not alter the existing list.

sorted(names, reverse=True)     # Sorts the List in Decending Order

names.index('google')       # Returns the index of the item in the List

print('yahoo' in names)    # Returns True if the item present in the List

# Converting Lists to String
print('-'.join(names))  # Prints yahoo-netflix-microsoft-instagram-google-gmail-facebook-apple-amazon
print('|'.join(names))  # Prints yahoo|netflix|microsoft|instagram|google|gmail|facebook|apple|amazon
print(','.join(names))  # Prints yahoo,netflix,microsoft,instagram,google,gmail,facebook,apple,amazon

# Slicing List's
# names[start:stop:step]
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
#       [   0         1         2       3           4           5           6      ]
#       [  -7        -6        -5      -4          -3          -2          -1      ]
print(names[2:5])   # Prints all the items from 2nd index upto but not including 5th index.
print(names[:4])    # Prints all items from 0th index and upto 4th index, but not including 4th index.
print(names[2:])    # Prints all items from 2nd index till the end of the List.

# Expression inside square brackets
print(names[1 + 3])  # Prints 4th item of the list
print(names[1 - 3])  # Prints 5th item of the list

# Slicing using negative indexing
print(names[-1])    # Prints the last index item of the list
print(names[-7])    # Prints the 0th index item of the list
print(names[-4:-2])     # Prints ['amazon', 'facebook']
print(names[-6:5])      # prints ['google', 'yahoo', 'amazon', 'facebook', 'instagram']
print(names[1:-1])      # prints ['google', 'yahoo', 'amazon', 'facebook', 'instagram']
print(names[:-1])   # Prints ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram']

print(names[:])     # Prints the entire list
print(names[::2])   # Prints alternate items in the list
print(names[::-1])  # Prints the items in the list in reverse order

print(names[::2])   # Prints alternate items in the list
print(names[2:7:2])
print(names[-1:2:-1])
print(names[::-1])      # Prints the list in Reverse order
# =========================================================================================
