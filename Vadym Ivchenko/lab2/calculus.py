c = input('Оберіть дію')

a = float(input('Введіть перше число :'))

b = float(input('Введіть друге число :'))

if c == '+':
    d = a+b
elif c == '-':
    d = a-b
elif c == '*':
    d =a*b
elif c == './.':
    d = a/b

print ('Результат :',d)
