def hg():
    print("Hi git")

hg()

# Функція з параметрами

def helloeveryone(nickname):
    print(f"Hello, {nickname}")

helloeveryone("@hitler")
helloeveryone("@boba")
helloeveryone("@mrboda")

# Значення по дефолту

def hello(name="boba"):
    print(f"Hello, {name}")

hello()
hello("biba")

# Іменовані параметри 

def person(name, age):
    print(f"Name: {name}, Age: {age}")

person(age=18, name="Boba")

# Невизначена кількість параметрів 

def sum(*numbers):
    result=0
    for n in numbers:
        result += n
    print(f"sum = {result}")

sum(1, 2, 3, 4)
sum(5, 6, 7, 8, 9)

# Повернення результату

def text():
    return "hi everyone"

message = text()
print(message)

print(text())