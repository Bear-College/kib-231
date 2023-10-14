# лямбда-вираз без параметрів 

massage = lambda: print("Hello world")

massage()

# лямбда-вираз з параметом

square = lambda n: n * n

print(square(8))

# лямбда-вираз з кількома параметрами

product = lambda a, b: a * b

print(product(3,2))

# передача лямбда-виразу як параметр

def do_op(a, b, op):
    result = op(a, b)
    print(f"Результат = {result}")

do_op(6, 7, lambda a, b: a+b)

