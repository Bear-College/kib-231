Fahrenheit = int(input('Type temperature in Fahrenheit: '))
Celsius = ((Fahrenheit-32)*5)/9
print(f"Temperature in Celsius is: {round(Celsius)}")

# Function
def converterTemperature(Fahrenheit):
    Celsius = ((Fahrenheit-32)*5)/9
    print(f"Temperature in Celsius is: {round(Celsius)}")

converterTemperature(int(input('Type temperature in Fahrenheit: ')))