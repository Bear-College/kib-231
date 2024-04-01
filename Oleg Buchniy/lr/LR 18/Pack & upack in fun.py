# Функція з використанням *args
def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

# Виклик функції з різною кількістю аргументів
greet('Alice', 'Bob', 'Charlie')
person_in_marketing=('David', 'Eve')
greet(*person_in_marketing)

# Функція з використанням **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Виклик функції з різними іменованими аргументами
print_info(name='John', age=30, city='New York')
person_in_engineer={"name":'Jane', "age":25, "country":'Canada', "occupation":'Engineer'}
print_info(**person_in_engineer)

