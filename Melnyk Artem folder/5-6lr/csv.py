import csv

FILENAME = "C:\Users\User\Desktop\Melnyk Artem\user.csv"

users = [
    ["Sergiy",32]
    ["Alice",20]
    ["Mike",25]
]

with open (FILENAME,"w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)


    with open (FILENAME,"a", newline="") as file:
        user = ["Sam",35]
         writer = csv.writer(file)
    writer.writerows(user)