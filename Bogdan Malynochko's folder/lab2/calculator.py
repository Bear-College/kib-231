a = input('Type first number: ');
b = input('Type second number: ');

operation = raw_input('Choose operation: '); # Just 'input' didn't work for me.

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