import csv
import pickle

text= input("Enter text: ")

with open("Yaroslav Hurskyi folder/lab5,6/file.txt", "w") as file:
        file.write (text)

with open("Yaroslav Hurskyi folder/lab5,6/file.txt", "r") as file:
        content = file.read()
        print(content)


name, age = input("Enter user info (name and age): ").split()      
user = [
        [name, age]
] 

with open("Yaroslav Hurskyi folder/lab5,6/file.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(user)

with open("Yaroslav Hurskyi folder/lab5,6/file.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
                print("Name:",row[0],"\tAge:",row[1])

with open("Yaroslav Hurskyi folder/lab5,6/file.dat", "wb") as file:
        pickle.dump(user, file)

with open("Yaroslav Hurskyi folder/lab5,6/file.dat", "rb") as file:
        content2 = pickle.load(file)
        for user in content2:
                print("Name:", user[0], "\tAge:", user[1])

