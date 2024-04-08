# While 
account = 20

while account > 0:
    print(f"Залишилось акаунтівв = {account}")
    account -=1
else:
    print(f"Залишилось акаунтів = {account} . Закінчилися")
print("I need more bullets!")

# For
message = "3450D"
for c in message:
    print(c)
else:
    print(f"Останній символ: {c} . Цикл завершений");
print("Робота програми завершена") 

# Nested cycles
i=1
j=1
while i < 10:
    while j < 10:
        print(i - j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1


# Brake and continue
number=15

while number > 0:
    number -= 3
    if number == 6:
        continue
    if number == 3:
        break
    print(f"number = {number}")
 