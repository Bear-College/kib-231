#Calculator 2.0
def Do_Calculation(a,b,operation):
    Calculation=operation(a,b)
    print(f"Result operation = {Calculation}")

print("Chouse operation :")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
print("5. Ділення націло")
print("6. Зведення в степінь")
print("7. Залишок від ділення")

choice=input("Your choise : ")
if choice == '1':
    Do_Calculation(int(input("Введіть число 1: ")),int(input("Введіть число 2: ")),lambda a,b : a+b)
elif choice == '2':
    Do_Calculation(int(input("Введіть число 1: ")),int(input("Введіть число 2: ")),lambda a,b : a-b)
elif choice == '3':
    Do_Calculation(int(input("Введіть число 1: ")),int(input("Введіть число 2: ")),lambda a,b : a*b)
elif choice == '4':
    Do_Calculation(int(input("Введіть число 1: ")),int(input("Введіть число 2: (не 0) ")),lambda a,b : a/b)
elif choice == '5':
    Do_Calculation(int(input("Введіть число 1: ")),int(input("Введіть число 2: ")),lambda a,b : a//b)
elif choice == '6':
    Do_Calculation(int(input("Введіть число 1: ")),int(input("Введіть число 2: ")),lambda a,b : a**b)
elif choice == '7':
    Do_Calculation(int(input("Введіть число 1: ")),int(input("Введіть число 2: ")),lambda a,b : a%b)
else:
    print("Невірний вибір операції")