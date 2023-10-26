

name = "Vlad"

def say_hi():
    global name #changes the variable to global and everything defined under "global" in this function, will be changed globally
    name = "Maria"
    print("Hi", name)

def say_bye():
    print("Bye", name)


def outer():
    n = 10
    def inner():
        nonlocal n
        n = 25
        print(n)

    inner() #25
    print(n)


say_hi()
say_bye()


outer()
