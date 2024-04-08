def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)  # Виведе: 1 2 3
def my_function(a, b, c):
    print(a, b, c)

my_tuple = (1, 2, 3)
my_function(*my_tuple)  # Розпаковує кортеж та передає його як аргументи функції