number=10

while number > 0:
    number -= 1
    if number == 5:
        continue
    if number == 2:
        break
    print(f"number = {number}")