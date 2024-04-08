import csv
import pickle

TXTFILE = "C:\\Users\\Super\\Desktop\\Artem Sheigets\\Artem Sheigets folder\\lab5-6\\task56.txt"
CSVFILE = "C:\\Users\\Super\\Desktop\\Artem Sheigets\\Artem Sheigets folder\\lab5-6\\task56.csv"
PICKFILE = "C:\\Users\\Super\\Desktop\\Artem Sheigets\\Artem Sheigets folder\\lab5-6\\task56.dat"

def write_to_txt(data):
    with open(TXTFILE, 'w') as file:
        for item in data:
            file.write(item + '\n')

def write_to_csv(data):
    with open(CSVFILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def write_to_binary(data):
    with open(PICKFILE, 'wb') as file:
        pickle.dump(data, file)

def read_from_txt():
    with open(TXTFILE, 'r') as file:
        data = file.readlines()
        for line in data:
            print(line.strip())

def read_from_csv():
    with open(CSVFILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

def read_from_binary():
    with open(PICKFILE, 'rb') as file:
        data = pickle.load(file)
        print(data)

def main():
    user_data = []
    while True:
        user_input = input("Введіть рядок (або 'done' для завершення введення): ")
        if user_input == 'done':
            break
        user_data.append(user_input)

    print("Запис до файлів:")
    write_to_txt(user_data)
    write_to_csv(user_data)
    write_to_binary(user_data)

    print("\nЗчитування та виведення з файлів:")
    print("З TXT файлу:")
    read_from_txt()
    print("\nЗ CSV файлу:")
    read_from_csv()
    print("\nЗ бінарного файлу:")
    read_from_binary()

if __name__ == "__main__":
    main()