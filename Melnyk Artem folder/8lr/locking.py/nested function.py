def outer_function(outer_variable):
    # Вкладена функція використовує параметр outer_variable зовнішньої функції
    def nested_function(inner_variable):
        result = outer_variable + inner_variable
        print("Результат обчислення у вкладеній функції:", result)

    # Викликаємо вкладену функцію
    nested_function(5)

# Виклик зовнішньої функції
outer_function(10)