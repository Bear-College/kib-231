a = int(input('Type first number: '));
b = int(input('Type second number: '));

operation = input('Choose operation: ');

if operation == '+':
    c = a + b
    print(c)
elif operation == '-':
    c = a - b
    print(c)
elif operation == '/':
    c = a / b
    print(c)
elif operation == '*':
    c = a * b
    print(c)
else:
    print("Invalid operation");