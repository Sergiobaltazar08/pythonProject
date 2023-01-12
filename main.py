# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# First basic module phyton, define variables
# "str" change the variable "int" to "String"



nombre = 'Sergio'
edad = 25
print( 'Hola mundo, soy ' + nombre + ' y tengo ' +str(edad) + ' años')

#we can save the information in the variable like this

nombre = 'David'
text = 'Hola mundo, soy ' + nombre + ' y tengo ' +str(edad) + ' años'
print(text)

#User Input: we can instruct Python to pause and read data from the user using the imput() function
#the input function return the string

nam = input('Who are you? ') #we need to write the name in the console example : Sergio
print('Welcome', nam)

# with input() we can add number the we can use other operator to operate with int.
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)

width = 15
height = 12.0
print(height / 3)
