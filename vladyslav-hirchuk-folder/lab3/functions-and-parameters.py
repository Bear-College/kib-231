
#functions-and-parameters

def say_something(i):
    name = "Bob"
    num = 1
    print(f"Hello, {name}! {i}")

    return num*i 

    

for x in range(0,5):
    b = say_something(x)

    print(f"Returned number: {b}")
