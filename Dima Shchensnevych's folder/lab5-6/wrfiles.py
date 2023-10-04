import csv
text= input("Введіть текст: ")

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile.txt", "w") as file:
        file.write (text)

with open("C:\DIMA SHCHENSNEVYCH\PythonBachelor\Dima Shchensnevych's folder\lab5-6\myfile.txt", "r") as file:
        conten = file.read()
        print(conten)


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
                print(row[0], " - " ,row[1])


