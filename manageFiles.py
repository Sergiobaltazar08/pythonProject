# What is a Handle?
print('---------------------------------------')
fhand = open('doc.txt')
print(fhand)

# The new line Character '\n'
print('---------------------------------------')
stuff = 'Hello\nWorld!'
print(stuff)

stuff = 'X\nY'
print(stuff)
# count the character in the line X\nY to X is 1, \n is 2 and Y is 3 with len we have 3
print(len(stuff))

# File Handle as a Sequence A 'file handle' open for read can be treated as a 'sequence' of string where each line in
# the file is a string in the sequence
print('---------------------------------------')
xfile = open('doc.txt')
for cheese in xfile:
    print(cheese)

# Counting lines in a File
print('---------------------------------------')
fhand = open('doc.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

# Reading the 'Whole' File
# We can read the whole file (newlines and all) into a single string
print('---------------------------------------')
fhand = open('doc.txt')
inp = fhand.read()
print(len(inp))
print(inp[:16])
print(inp[26:41])

# Searching Through a File
# We can put an if statement in our for loop to only print lines that meet some criteria
print('---------------------------------------')
fhand = open('doc.txt')
for line in fhand:
    if line.startswith('Name'):
        print(line)
# Searching Through a File(FIXED)
# The newline is considered "white space" and is stripped
print('---------------------------------------')
fhand = open('doc.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('Name'):
        print(line)

# TSkipping with continue
# We can conveniently skip a line by using the continue statement
print('---------------------------------------')
fhand = open('doc.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Name'):
        continue
    print(line)

# Using 'in' to select lines
print('---------------------------------------')
fhand = open('doc.txt')
for line in fhand:
    line = line.rstrip()
    if not '@gmail.com.bo' in line:
        continue
    print(line)

# Bad File Names good name example is doc.txt the bad name of the file is 'na boo na boa'
print('---------------------------------------')
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('email'):
        count = count + 1
print('There were', count, 'email line in', fname)
