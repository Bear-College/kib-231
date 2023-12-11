op=input("Яку операію слід виконати +, -, *, /, //, ** або % :")

a=float(input("Введіт перше число :"))

b=float(input("Введіт друге число :"))

if op == "+":
    c=a+b
    print(c)
elif op == "-":
    c=a-b
    print(c)
elif op == "*":
    c=a*b
    print(c)
elif op == "/":
    c=a/b
    print(c)
elif op == "//":
    c=a//b
    print(c)
elif op == "**":
    c=a**b
    print(c)
elif op == "%":
    c=a%b
    print(c)
else:
    print("Введено невірну операцію!")