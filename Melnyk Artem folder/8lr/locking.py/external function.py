def outer_function(outer_variable):
    # Параметр outer_variable та локальна змінна inner_variable входять в лексичне оточення inner_function
    def inner_function(inner_variable):
        result = outer_variable + inner_variable
        print("Результат обчислення у внутрішній функції:", result)

    # Викликаємо внутрішню функцію
    inner_function(5)

# Виклик зовнішньої функції
outer_function(10)