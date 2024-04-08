squares = [x ** 2 for x in range(1, 11)]

print(" Використання list comprehension для створення списку квадратів чисел від 1 до 10")
print("Квадрати чисел від 1 до 10:", squares)


even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print(" Використання list comprehension для створення списку парних чисел від 1 до 20")
print("Парні числа від 1 до 20:", even_numbers)

