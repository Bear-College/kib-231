import csv
import pickle

def write_to_txt(data):
    with open('data.txt', 'w') as txt_file:
        for line in data:
            txt_file.write(line + '\n')

def write_to_csv(data):
    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)

def write_to_binary(data):
    with open('data.bin', 'wb') as binary_file:
        pickle.dump(data, binary_file)

def read_and_print(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f'Зчитано з {file_name}:\n{content}')
    except FileNotFoundError:
        print(f'Файл {file_name} не знайдено.')

# Користувач вводить масив рядків
user_input = input("Введіть масив рядків (розділіть їх комою): ")
user_data = user_input.split(',')

# Записуємо в різні файли
write_to_txt(user_data)
write_to_csv(user_data)
write_to_binary(user_data)

# Зчитуємо та виводимо дані з різних файлів
read_and_print('data.txt')
read_and_print('data.csv')
read_and_print('data.bin')