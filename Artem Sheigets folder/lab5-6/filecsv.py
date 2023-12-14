import csv
FILENAME = "C:\\Users\\Super\\Desktop\\Artem Sheigets\\Artem Sheigets folder\\lab5-6\\user.csv"

users = (
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
)

with open(FILENAME, "w", newline="")as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, "a", newline="")as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)