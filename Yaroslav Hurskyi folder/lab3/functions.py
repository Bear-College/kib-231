# Функція з параметрами

def helloeveryone(nickname):
    print(f"Hello, {nickname}")

helloeveryone("Nezox")
helloeveryone("DOTA")

# Значення по дефолту

def hello(name="Nezox"):
    print(f"Hello, {name}")

hello()
hello("DOTA")

# Іменовані параметри 

def person(name, age):
    print(f"Name: {name}, Age: {age}")

person(age=18, name="NEZOX")

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
    return "HI everyone"

message = text()
print(message)

print(text())