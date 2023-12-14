c = input('Виберіть дію')
a = int (input('Введіть перше число :'))
b = int (input('Введіть друге число :'))

if c == '+':
    d = a+b
elif c == '-':
    d = a-b
elif c == '*':
    d =a*b
elif c == '/':
    d = a/b
print ('Відповідь :',d)