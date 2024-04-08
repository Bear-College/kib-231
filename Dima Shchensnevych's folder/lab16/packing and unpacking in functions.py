def mult(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(mult(1,2))
print(mult(1,2,3))
print(mult(1,2,3,4))

print("-----------------------------")

def user(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

user(name = "Bob", age = "40", company = "Apple")

print("-----------------------------")

numbers = (1,2,3,4,5)
print(mult(*numbers))

print("-----------------------------")

def print_person(name, age, company):
    print(f"Name:{name}, Age:{age}, Company:{company}")
Bob = {"name": "Bob", "age": 40, "company": "Apple" }
print_person(**Bob)

print("-----------------------------")

def sum(num1, num2, *nums):
    result=num1+num2
    for n in nums:
        result+=n
    return result

print(sum(1,2,3,4))
print(sum(1,2,3,4,5))