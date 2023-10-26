name = "Tom"

def say_hi():
    global name
    name = "Bob"
    print("Hello", name)

def say_bye():
    print("good bye",name)

say_hi()
say_bye()