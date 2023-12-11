def custom_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Результат функції: {result}")
        return result  # Можна виконати деякі додаткові операції з результатом перед його поверненням
    return wrapper

# Використовуємо декоратор
@custom_decorator
def add_numbers(a, b):
    return a + b

# Викликаємо декоровану функцію
result = add_numbers(3, 5)
print("Загальний результат:", result)