Far = float(input("Температура в градусах Фаренгейта:"))

def conversion():
    Cel = ((Far-32)*5)/9
    print(f"Температура в градусах Цельсія: {Cel}")

conversion()