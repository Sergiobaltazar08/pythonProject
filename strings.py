# String Data Type
print('------------------------------------')
str1 = "Hello"
str2 = "there"
bob = str1 + str2
print(bob)
str3 = '123'
str3 = int(str3) + 1
print(str3)

# Read and converting
print('------------------------------------')
name = input('Enter Name: ')
print(name)

apple = input('Enter int: ')
x = int(apple) - 10
print(x)

# Looking Inside String
# We can get at any single character in a string using an index specified in square brackets
# the inter value must be an integer and start at zero
# |b|a|n|a|n|a|
# |0|1|2|3|4|5|
print('------------------------------------')
fruit = 'banana'
letter = fruit[1]
print(letter)

x = 3
w = fruit[x - 1]
print(w)

# Looping Through String by 'while'
print('------------------------------------')
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# Looping Through String by 'for'
print('------------------------------------')
fruit = 'banana'
for letter in fruit:
    print(letter)

# What will the following code print?:
print('------------------------------------')
for new in "banana":
    print(new)


# Slicing String
# we can also look at any continuous section fo a string using a colon operator
print('------------------------------------')
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])

# we can skip some expressions
print(s[:2])
print(s[8:])
print(s[:])

# String Concatenation
# When the '+' operator is applied to string it means concatenation
print('------------------------------------')
a = 'Hello'
b = a + 'there'
print(b)
c = a + ' ' + 'there'
print(c)

# Using 'in' as a logical Operator
# The 'in' keyword can also be used to check to seee if one string is  'in' another string
print('------------------------------------')
fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit :
    print('Found it!')

# String Comparison
print('------------------------------------')
word = 'banana'
if word == 'banana':
    print('All right, banana')

if word < 'banana':
    print('You word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, banana.')

# String Library
print('------------------------------------')
greet = ' Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi there'.lower())
print('------------------------------------')
stuff = 'Hello world'
print(type(stuff))

print(dir(stuff))

# Searching a String
print('------------------------------------')
fruit = ' banana'
pos = fruit.find('na')
print(pos)
aa = fruit.find('z')
print(aa)

# Making everything UPPER CASE
# You can make a copy of a string in lower case or upper case
print('------------------------------------')
greet = ' Hello Bob'
nnn = greet.upper()
print(nnn)
www = greet.lower()
print(www)

# Search and Replace
# the 'replace()' function is like a "search and replace" operation in a word processsor
print('------------------------------------')
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'x')
print(nstr)

# Stripping Whitespace
# Sometimes we want to take a string and remove whitespace at the beginning and/or end
print('------------------------------------')
greet = '   Hello Bob    '
# remove whitespace at the beginning
print(greet.lstrip())
# remove whitespace at the end
print(greet.rstrip())
# remove whitespace both
print(greet.strip())

# Parsing and Extracting
print('------------------------------------')
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1: sppos]
print(host)

