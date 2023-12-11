# Цикл While
clients= 6

while clients > 0:
    print(f"Залишилось клієнтів - {clients}")
    clients -= 1
else:
    print(f"Залишилось клієнтів - {clients}. Всі клієнти обслуговані")

print("Робочий день завершено")

# Цикл for
name = "DIMA"
for c in name:
    print(c)
else:
    print(f"Остання буква - {c}. Цикл завершено")
    
print("Програму завершено")