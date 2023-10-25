                            #Отримання параметрів функції у декораторі
#Декоратор - це функція, яка додає функціональність іншій функції без її зміни.
# визначення функції декоратора
def check(input_func):    
    def output_func(*args):
        name = args[0]
        age = args[1]           # отримуємо значення другого параметра
        if age < 0: age = 1     # якщо вік <0, змінюємо його значення на 1
        input_func(name, age)   # передаємо функції значення для параметрів
    return output_func
 
# визначення оригінальної функції
@check
def print_person(name, age):
    print(f"Name: {name}  Age: {age}")
 
# виклик оригінальної функції
print_person("Tom", 38)
print_person("Bob", -5)