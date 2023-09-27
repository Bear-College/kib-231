number=15

while number > 0:
    number -= 3
    if number == 6:
        continue
    if number == 3:
        break
    print(f"number = {number}")