text = input("Ведіть текст: ")
word = text.split()
first_character = [word[0] for word in word]
result = ''.join(first_character)
print(f"Перша літера: {first_character}")