#first we define our values in 'def', then we can call our function
def thing():
    print('Hello')
    print('Fun')

#we call our function thing

thing()
print('Zip')
thing()

# Our function in python are print() input() type() float() int().....
# Functions that we define ourselves and then use

# int the max value is 'w'(a string) and the small function is blanc
print('------------------------------')
big = max('Hello world')
print(big)

tiny = min ('Hello World')
print(tiny)

# type Conversions
print('------------------------------')

print (float(99) / 100)

i = 42
type(i)
#<class 'int'>

f = float(i)
print(f)
type(f)
#<class 'float'>

print(1 + 2 * float(3) / 4 - 5)

#String Covenrsions if the string doesn't have a number the string must not trasform to int
print('------------------------------')
sval = '123'
type(sval)
print(sval)
ival = int(sval)
print(ival + 1)

#more functions
print('------------------------------')
x = 5
print('Hello')
def print_lyrics() :
    print("I'm a  lumberjack, and I'm okay")
    print('I sleep all night and I work all day.')

print('Yo')
print_lyrics()
x = x +2
print(x)


#we define the parameters is a variable which we use in the function
print('------------------------------')
def greet(lang) :
    if lang == 'es' :
        print('Hola')
    elif lang == 'fr' :
        print('Bongjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fr')

#
print('------------------------------')


#What will the following Python program print out?:
print('------------------------------')
def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()