import os
import csv
import pickle
directory_path = r'C:\Users\user\Desktop\CUM ZONE\PythonBachelor\Bogdan Erebakan folder\lr 5,6'

def main():
    input_strings = input("Ведіть текст (розділяйте комами): ").split(',')
    save_to_txt(input_strings)
    save_to_csv(input_strings)
    save_to_binary(input_strings)

    read_and_display_txt()
    read_and_display_csv()
    read_and_display_binary()

def save_to_txt(data):
    file_path = os.path.join(directory_path, "data.txt")
    with open(file_path, "w") as txt_file:
        txt_file.write("\n".join(data))

def save_to_csv(data):
    file_path = os.path.join(directory_path, "data.csv")
    with open(file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)

def save_to_binary(data):
    file_path = os.path.join(directory_path, "data.bin")
    with open(file_path, "wb") as bin_file:
        pickle.dump(data, bin_file)

def read_and_display_txt():
    file_path = os.path.join(directory_path, "data.txt")
    if os.path.exists(file_path):
        with open(file_path, "r") as txt_file:
            data = txt_file.read()
            print("шось натикане в data.txt:")
            print(data)

def read_and_display_csv():
    file_path = os.path.join(directory_path, "data.csv")
    if os.path.exists(file_path):
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            data = next(csv_reader)
            print("шось натикане в  data.csv:")
            print(data)

def read_and_display_binary():
    file_path = os.path.join(directory_path, "data.bin")
    if os.path.exists(file_path):
        with open(file_path, "rb") as bin_file:
            data = pickle.load(bin_file)
            print("шось натикане в  data.bin:")
            print(data)

if __name__ == "__main__":
    main()
 