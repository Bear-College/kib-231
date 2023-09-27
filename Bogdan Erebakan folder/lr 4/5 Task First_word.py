input_text = input("Введіть текст: ")
word = input_text.split()
First_WRD = [word[0] for word in word]
result = ''.join(First_WRD)
print("Перші букви кожного слова:", result)
