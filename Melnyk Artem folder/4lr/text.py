def extract_first_letters(text):
    words = text.split()
    first_letters = [word[0] for word in words]
    return ''.join(first_letters)

# Зчитуємо текст від користувача
input_text = input("Введіть текст: ")

# Отримуємо та виводимо перші букви кожного слова
result = extract_first_letters(input_text)
print("Перші букви кожного слова:", result)