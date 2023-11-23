try:
    number1=int(input("Тикни перше число"))
    number2=int(input("Тикни друге число"))
    print("Результат ділення:",number1/number2)
except (ZeroDivisionError,ValueError):
    print("NISE TRY CID")

print("ADIOS")