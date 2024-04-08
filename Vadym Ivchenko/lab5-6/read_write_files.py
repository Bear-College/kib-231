import csv
import pickle

text= input("введіть текст: ")

with open("Vadym Ivchenko/lab5-6/file.txt", "w") as file:
        file.write (text)

with open("YVadym Ivchenko/lab5-6/file.txt", "r") as file:
        content = file.read()
        print(content)


name, age = input("введіть інформацію (імя та вік): ").split()      
user = [
        [name, age]
] 

with open("Vadym Ivchenko/lab5-6/file.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(user)

with open("Vadym Ivchenko/lab5-6/file.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
                print("Імя:",row[0],"\tВік:",row[1])

with open("Vadym Ivchenko/lab5-6/file.dat", "wb") as file:
        pickle.dump(user, file)

with open("Vadym Ivchenko/lab5-6/file.dat", "rb") as file:
        content2 = pickle.load(file)
        for user in content2:
                print("Імя:", user[0], "\tВік:", user[1])

