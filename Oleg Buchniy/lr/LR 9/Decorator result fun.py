# визначення функції декоратора
def check(input_func):    
    def output_func(*args):
        result = input_func(*args)   # передаємо функції значення для параметрів
        if result < 0: result = 0   # якщо результат функції менший за нуль, то повертаємо 0
        return result
    return output_func
 
# визначення оригінальної функції
@check
def sum(a, b):
    return a + b
 
# виклик оригінальної функції
result1 = sum(10, 20)
print(result1)          # 30
 
result2 = sum(10, -20)
print(result2)          # 0