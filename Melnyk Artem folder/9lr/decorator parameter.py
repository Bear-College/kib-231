def custom_decorator(parameter):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Декоратор отримав параметр: {parameter}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Використовуємо декоратор з параметром
@custom_decorator("Це параметр декоратора")
def my_function():
    print("Виклик моєї функції")

# Викликаємо функцію
my_function()