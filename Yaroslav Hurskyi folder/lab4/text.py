text = input("введіть текст: ")

first_letters = ""

for word in text.split():
    if word:
        first_letters += "\n" + word[0]

print("перші букви кожного слова:",first_letters)