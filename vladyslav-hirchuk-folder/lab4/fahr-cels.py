

def fahrenheit_celsius(f):
    cels = (f - 32) * 5/9
    return cels

def main():
    fahr = float(input("Fahrenheit: "))

    print(fahrenheit_celsius(fahr))


main()

