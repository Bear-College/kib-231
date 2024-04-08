names_list=[
    [1,"Dima"],
    [2,"Pasha"],
    [3,"Max"]
]

users=dict(names_list)
print(users)

print("--------------------------------------------------------------")

users[3]="Lebron James"
print(users)

print("--------------------------------------------------------------")

users[4]='Jimmy "The REV" Sullivan'
user4=users.get(4)
print(user4)
print(users)

print("--------------------------------------------------------------")

del users[3]
print(users)

print("--------------------------------------------------------------")

user=users.pop(2)
print(user)
print(users)

print("--------------------------------------------------------------")

users1=users.copy()
print(users1)

print("--------------------------------------------------------------")

print(users)
users.clear()
print(users)

print("--------------------------------------------------------------")

users2 = {2: "II", 3 : "Chad Smith" }
users1.update(users2)
print(users1)
print(users2)

print("--------------------------------------------------------------")

for key in users1:
    print(f"Key:{key} User:{users1[key]}")

print("--------------------------------------------------------------")

for key, value in users1.items():
    print(f"Key:{key} User:{value}")

print("--------------------------------------------------------------")

users = {
    "Dima":{
        "phone": "+2232312314",
        "email": "dima@gmail.com"
    },
    "Pasha":{
        "phone": "+1211123212",
        "email": "pasha@gmail.com",
        "discord": "pasha321"
    }
}
users["Dima"]["email"] = "superdima@gmail.com"
print(users["Dima"])

print("--------------------------------------------------------------")

#dima_discord = users["Dima"]["discord"]

key = "discord"
if key in users["Dima"]:
    print(users["Dima"]["discord"])
else:
    print("discord not found")