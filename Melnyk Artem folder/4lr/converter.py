f = int(input('Введіть температуру в °F'))
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Зчитуємо температуру в градусах Фаренгейта від користувача
fahrenheit_temperature = float(input("Введіть температуру в градусах Фаренгейта: "))

# Конвертуємо температуру
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

# Виводимо результат
print(f"{fahrenheit_temperature} градусів Фаренгейта дорівнюють {celsius_temperature:.2f} градусам Цельсія.")