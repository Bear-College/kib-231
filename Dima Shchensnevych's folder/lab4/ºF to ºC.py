F=float(input("Введіть значення температури в ºF:"))

def convert():
    C=(F-32)/1.8
    print(f"Температура {C} ºC" )

convert()