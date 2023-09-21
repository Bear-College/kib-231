f = float(input("Введіть температуру в градусах Фаренгейта: "))
def fahrenheit_to_celsius(f):
    c = (f - 32) /1.8
    return c
c = fahrenheit_to_celsius(f)
print(f"{f} градусів Фаренгейта дорівнює {c} градусам Цельсія.")
 
print("Прога все зробила")