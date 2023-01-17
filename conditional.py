# Comparison Operators
# Python  |      <      |      <=                 |       ==
# Meaning |  Less than  |  Less than or Equal to  |   Equal to

# Python  |         >=                  |   >               |    !=
# Meaning | Greater than or Equal to    |   Greater than    | Not equal

# we can define 'elif' is the condicion to go 'else' and ask the other 'if' but if the first condicion is right the process will finish

x = 7
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else:
    print('LARGE')
print('All done')

# other example is :
x = 5000
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('big')
elif x < 40 :
    print('Large')
elif x < 100 :
    print('Huge')
else:
    print('Ginormous')
print('All done')



