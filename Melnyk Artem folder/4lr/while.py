while True:
    user_input = input("Введіть текст: ")
    if user_input.lower() == "stop":
        print("Програма зупинена.")
        break
    else:
        print("Ви ввели:", user_input)