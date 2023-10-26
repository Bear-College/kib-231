import csv
import pickle

def txtwrite(warr):
    with open("text.txt", "a") as myfile:
        for x in warr:
            myfile.write(f"{x}\n")

def txtread():
    with open("text.txt", "r") as myfile:
        for line in myfile:
            print(line.strip())

def csvread():
    with open("csvtext.csv", "r", newline="") as myfile:
        reader = csv.reader(myfile)
        for row in reader:
            print(''.join(row))

def binread():
    with open("bintext.dat", "rb") as myfile:
        text = pickle.load(myfile)
        for i in text:
            print(i)

def csvwrite(warr):
    with open("csvtext.csv", "a", newline="") as myfile:
        writer = csv.writer(myfile)
        for i in warr:
            writer.writerow([i])

def binwrite(warr):
    with open("bintext.dat", "wb") as file:
        pickle.dump(warr, file)

def main():
    while True:
        print("1. add some strings and create files")
        print("2. read files")
        print("3. exit the program")

        choice = int(input("Choice: "))

        if choice == 1:
            n = int(input("how many strings: "))
            arr = []
            for i in range(n):
                word = input(f"{i}. word: ")
                arr.append(word)

            txtwrite(arr)
            csvwrite(arr)
            binwrite(arr)
        elif choice == 2:
            print("txtread: ")
            txtread()
            print("csvread: ")
            csvread()
            print("binread: ")
            binread()
        elif choice == 3:
            exit()

if __name__ == "__main__":
    main()
