name = "Vadym"

def say_hi():
    global name
    name = "Vladim"
    print("Hi", name)

def say_bye():
    print("BY",name)

say_hi()
say_bye()