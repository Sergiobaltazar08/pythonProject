#Loops and Iterations
#repeated Steps by 'while'
print('------------------------------')
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff!')
print(n)

#repeated Steps : Infinity loop if n = 1 or more than 0
print('------------------------------')
n = 0
while n > 0:
    print('Lather')
    print('Rinse')
print('Dry off!!')

#repeated Steps : Breaking Out of a Loop
print('------------------------------')
while True:
    print('Type: done')
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')


#What will the following code print out?: 0 1 2
print('------------------------------')
ns = 0
while True:
    if ns == 3:
        break
    print(ns)
    ns = ns + 1

#'For' Loop
#A simple definite loop
print('------------------------------')

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')

#A definite Loop with String
print('------------------------------')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

#How many lines will the following code print?: 3
print('------------------------------')
for i in [2, 1, 5]:
    print(i)

#Making "smart" Loops
#looping through a Set
print('------------------------------')
print('Before')
for thing in [9, 41, 12, 3, 74, 15]:
    print(thing)
print('After')

#Finding the largest value
print('------------------------------')
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

#Below is code to find the smallest value from a list of values. One line has an error that will cause the code to not work as expected. Which line is it?: 6
print('------------------------------')
smallest = None
print("Before:", smallest)
for iter_var in [6, 41, 12, 9, 74, 15]:
    if smallest is None or iter_var < smallest:
        smallest = iter_var
        break
    print("Loop:", iter_var, smallest)
print("Smallest:", smallest)

# Summing in a Loop
print('------------------------------')
number = 0
print("Before:", number)
for thing in [6, 41, 12, 9, 74, 15]:
    number = number + thing
    print(number, thing)
print('After', number)

# Finding the Average in a Loop
print('------------------------------')

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)

# Finding in a Loop
print('------------------------------')

print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print('Large number', value)
print('After')

# Search Using a boolean Variable
print('------------------------------')

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

# Finding the smallest value
print('------------------------------')

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

# How can we use the "is" and "is not" Operators  just we can use in boolean or None values
print('------------------------------')

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)













