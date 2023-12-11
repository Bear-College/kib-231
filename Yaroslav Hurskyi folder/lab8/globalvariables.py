name = "Yaroslav"

def say_hi():
    global name
    name = "Nezox"
    print("hello", name)

def say_bye():
    print("good bye",name)

say_hi()
say_bye()