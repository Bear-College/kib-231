text = input("Введіть текст: ")

first_letters = ""

for word in text.split():
    if word:
        first_letters += word[0]

print("Перші букви кожного слова:",first_letters)