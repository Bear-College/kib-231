c = input('Вибери дію')

a = int (input('Введи перше число :'))

b = int (input('Введи друге число :'))

if c == '+':
    d = a+b
elif c == '-':
    d = a-b
elif c == '*':
    d =a*b
elif c == './.':
    d = a/b

print ('Результат :',d)