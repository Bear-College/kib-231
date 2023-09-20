# Just a function
def myFirstFunctionInPythonEver():
    print('Hello World');

myFirstFunctionInPythonEver();

# Function with parameters
def saySomething(data):
    print(f"You've written: {data}");

saySomething(data = input('Type name: '));

# Function with returning data
def calculateNumbers(a, b):
    return print(a + b);

calculateNumbers(a = 5, b = 6);

# Function with array and loop
def sum (numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)

sum(numbers = [2, 5, 34, 322, 233, 113313, 100]);

