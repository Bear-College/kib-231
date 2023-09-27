# While 
ammunition = 20

while ammunition > 0:
    print(f"Залишилось набоїв = {ammunition}")
    ammunition -=1
else:
    print(f"Залишилось набоїв = {ammunition} . Набої скінчилися")
print("I need more bullets!")

# For
message = "3450D"
for c in message:
    print(c)
else:
    print(f"Останній символ: {c} . Цикл завершений");
print("Робота програми завершена") 