try:
     x = 10 / 0  
except ZeroDivisionError as e:
    print(f"Виникла помилка: {e}")
except Exception as e:
    print(f"Загальна помилка: {e}")
finally:
    print("Блок finally ")
print("Продовження ")
