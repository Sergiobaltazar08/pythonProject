# Programming Algorithms and Data Structures
# A list is a kind of collection
# A collection allows us to put many values in a single "variable"

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']

# List Constants
# we can print many differnt items like int, string, dooble or empty list
print('------------------------------------')
print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([1, [5, 6], 7])
print([])

# We already use list!
print('------------------------------------')
for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

# List and fefinite loops - best pals
print('------------------------------------')
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('Done!')
# Looking Inside List
print('------------------------------------')
# Positions     0       1        2
friends = ['Joseph', 'Glenn', 'Sally']
print(friends[1])

# Lists are Mutable
# List are "mutable" we can change an element of a list using the index operator
print('------------------------------------')
fruit = 'Banana'
# fruit[0] = 'b'

x = fruit.lower()
print(x)

lotto = [2, 14, 32, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

# How long is a List?
# the len() function takes a list as a parameter and returns the number of elements in the list
print('------------------------------------')

greet = 'Hello Bob'
print(len(greet))

x = [1, 2, 'joe', 99]
print(len(x))

# Using the range function
# the range function returns a list of numbers that range from zero to one less that the parameter
print('------------------------------------')

print(range(4))
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))
print('------------------------------------')
friends = ['Joseph', 'Glenn', 'Sally']
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year: ', friend)

# What is the value of x after running this code:
print('------------------------------------')
fruit = "banana"
x = fruit[1]
print(x)

# CONCATENATION LIST USING "+"
# We can create a new list by adding two existing lists together
print('------------------------------------')
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)
# Lists can be sliced using
print('------------------------------------')
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# List Methods
print('------------------------------------')
x = list()
print(type(x))
print(dir(x))

# Building a List from Scratch
# We can create an empty list and then add elements using the append method
print('------------------------------------')
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)

# I Something in  a List?
# Python provides two operators that let you check if an item is in a list
# These are logical operators that return True or False
print('------------------------------------')
some = [1, 9, 21, 10, 16]
print(9 in some)
print(15 in some)
print(20 not in some)

# Lists are in Order
# The sort method (unlike in string) means "sort yourself"
print('------------------------------------')
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])

# Built-in Functions and List
print('------------------------------------')
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

print('------------------------------------')
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average: ', average)
