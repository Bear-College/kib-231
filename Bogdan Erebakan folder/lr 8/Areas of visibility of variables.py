name="BOda"
def say_hi():
    print("heeey",name) #Глобальний контекст

def say_bye():
    print("byyyyyyye",name)

say_hi()
say_bye()

def say_hayyy():
    name="xz"
    surname="mr"
    print("Heeeey",name,surname) # локальний контекст

def say_byyyye():
    name="lz"
    print("have a nice night",name)

say_hayyy()
say_byyyye()

def outer():
    n=9

    def inner():
        nonlocal n
        n=21
        print(n) #приховування змінних
    inner()
    print(n)

outer()