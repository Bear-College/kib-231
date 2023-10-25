def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        print(count)
    return increment

my_counter = counter() #increment-func
my_counter() #1
my_counter() #2
my_counter() #3


another_counter = counter()
another_counter() #1
