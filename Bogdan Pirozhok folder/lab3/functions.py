# Проста функція

def greeting():
    print("Hello")

greeting()

# Функція з параметром

def greeting(name):
    print(f"Hello, {name}")

greeting("Dima")

# Значення по дефолту 

def greeting(name="Misha"):
    print(f"Hello, {name}")

greeting()
greeting("Dima")

# Іменовані параметри 

def person(name, age):
    print(f"Name: {name}, Age: {age}")

person(age=19, name="Dima")

# Невизначена кількість параметрів 

def sum(*numbers):
    result=0
    for n in numbers:
        result += n
    print(f"sum = {result}")

sum(2, 4, 5, 6)

# Повернення значення 

def sum(number):
    return number+number

print(sum(5))