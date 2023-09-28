def Addition(x, y):
    return x + y

def Subtraction(x, y):
    return x - y

def Multiplication(x, y):
    return x * y

def Division(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x / y

def Division_By_A_Whole(x,y):
    return x // y 

def Pow(x,y):
    return x ** y

def Remainder(x,y):
    return x % y

def FromFloatToInt(x):
    return round(x)

print("Оберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
print("5. Ділення націло")
print("6. Зведення в степінь")
print("7. Залишок від ділення")
print("8. Округлення числа")


choice = input("Введіть номер операції (1/2/3/4/5/6/7/8): ")
'''
if choice == '8':
    number3 = float(input("Введіть перше число: "))

else:
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
'''
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
if choice == '1':
    print("Результат:", Addition(number1, number2))
elif choice == '2':
    print("Результат:", Subtraction(number1, number2))
elif choice == '3':
    print("Результат:", Multiplication(number1, number2))
elif choice == '4':
    print("Результат:", Division(number1, number2))
elif choice == '5':
    print("Результат:", Division_By_A_Whole(number1, number2))
elif choice == '6':
    print("Результат:", Pow(number1, number2))
elif choice == '7':
    print("Результат:", Remainder(number1, number2))
elif choice == '8':
    print("Результат:", FromFloatToInt(number1))
else:
    print("Невірний вибір операції")