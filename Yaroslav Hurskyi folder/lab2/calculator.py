c = input('Select operaion (+,-,*,/): ')
a = int (input('Type 1st numero :'))
b = int (input('Type 2nd numero :'))

if c == '+':
    d = a+b
elif c == '-':
    d = a-b
elif c == '*':
    d =a*b
elif c == '/':
    d = a/b
print ('Result :',d)