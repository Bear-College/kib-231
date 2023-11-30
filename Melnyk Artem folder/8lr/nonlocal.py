def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x += 5
        print("Змінна x у внутрішній функції:", x)

    inner_function()
    print("Змінна x у зовнішній функції:", x)

# Виклик зовнішньої функції
outer_function()