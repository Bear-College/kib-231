
#calculator

def addition():
    i = int(input("How many numbers you would like to add? "))
    summary = 0
    print("Enter numbers you would like to add: ")
    for x in range(0, i):
        num = float(input())
        summary += num

    print(summary)

def subtraction():
    i = int(input("How many numbers you would like to substract?"))
    summary = 0
    for x in range(0, i):
        num = float(input())
        if x == 0:
            summary = num
        else:
            summary -= num

    print(summary)

def multiplication():
    i = int(input("How many numbers you would like to multiply?"))
    summary = 1
    for x in range(0, i):
        num = float(input())
        summary *= num

    print(summary)

def division():
    i = int(input("How many numbers you would like to divide?"))
    summary = 0
    for x in range(0, i):
        num = float(input())
        if(x == 0):
            summary += num
        else:
            summary /= num

    print(summary)

def exponentiation():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    print(a**b)
    
def modulus():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(a % b)

def floorDivision():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(a // b)

while True:
    print("\n|------------------- Calculator -------------------|\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Modulus")
    print("7. Floor division")
    print("8. Exit")
    print("\n|------------------- ---------- -------------------|")
    print()

    choice = input("Choice: ")

    match choice:
        case "1":
            addition()
        case "2":
            subtraction()
        case "3":
            multiplication()
        case "4":
            division()
        case "5":
            exponentiation()
        case "6":
            modulus()
        case "7":
            floorDivision()
        case "8":
            exit()
        case _:
            continue

                


                
