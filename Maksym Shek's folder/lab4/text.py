text = input("Введіть текст: ")

first_letters = ""

for слово in text.split():
    if слово:
        first_letters += слово[0]

print("Перші букви кожного слова:", first_letters)