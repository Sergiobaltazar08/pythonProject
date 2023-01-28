# Dictionaries
# the most important in python
# we use the Collections
# Dictionaries example
print('----------------------------------------')
purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] =purse['candy'] + 2
print(purse)

# Comparing Lists and Dictionaries.
# Dictionaries are like except that they use keys instead of numbers to look up values
# In list the key is the position and in the dictionaries es the name
print('----------------------------------------')
print('Lists')
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0]=23
print(lst)
print('Dictionaries')
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

# Dictionary Literals(Constants)
# Use curly braces and have a list of key:value pairs
print('----------------------------------------')
jjj = {'chuck': 1, 'fred': 42,'jan': 100}
print(jjj)
ooo ={}
print(ooo)

# What does dict equal after running this code?:
print('----------------------------------------')
#dict = {"Fri": 20, "Thu": 6, "Sat": 1}
#dict["Thu"] = 13
#dict["Sat"] = 2
#dict["Sun"] = 9
#print(dict)

# MOST COMMON NAME?
# marquard, zhen, csev, sven

# Many Counters with a Dictionary
# One common use of dictionaries is counting how often we "see" something
print('----------------------------------------')
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# Dictionary Traceback
# We can use the 'in' operator to see if a key is in the dictionary
print('----------------------------------------')
ccc = dict()
print('csev' in ccc)

# When we see a new name
print('----------------------------------------')
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# The get method for dictionaries
print('----------------------------------------')
if name in counts:
    x = counts[name]
else:
    x = 0
x = counts.get(name, 0)
print(x)

# Simplified counting with get()
print('----------------------------------------')
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
   counts[name] = counts.get(name, 0) + 1
print(counts)

# What will the following code print?
print('----------------------------------------')
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))