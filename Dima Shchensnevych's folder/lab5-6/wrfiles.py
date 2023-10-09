import csv
import pickle

text= input("Введіть текст: ")

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile.txt", "w") as file:
        file.write (text)

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile.txt", "r") as file:
        content = file.read()
        print(content)


name, age = input("Введіть дані користувача: ").split()      
user = [
        [name, age]
] 

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile2.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(user)

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile2.csv", "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
                print("Ім'я:",row[0],"\tВік:",row[1])

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile3.dat", "wb") as file:
        pickle.dump(user, file)

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile3.dat", "rb") as file:
        content2 = pickle.load(file)
        for user in content2:
                print("Ім'я:", user[0], "\tВік:", user[1])

