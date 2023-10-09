              # Проста функція
def gr():
    print("Salam")
gr()
               # Функція з параметром
def gr(name):
    print(f"Salam, {name}")
gr("Boda")
                # Значення по дефолту 
def gr(name="Sanya"):
    print(f"Salam, {name}")
gr()
gr("Boda")
                   # Іменовані параметри 
def yours(name, age):
    print(f"Name: {name}, Age: {age}")
yours(age=21, name="Boda")
                   # Невизначена кількість параметрів 
def sum(*numbers):
    result=0
    for n in numbers:
        result += n
    print(f"sum = {result}")
sum(3, 5, 6, 7)
                    # Повернення значення 
def sum(number):
    return number+number
print(sum(5))