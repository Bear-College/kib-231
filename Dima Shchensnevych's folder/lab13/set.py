users_list = ["Dima", "Pasha", "Max"]
users=frozenset({"Dima", "Pasha", "Max"})
print(len(users))
users = set(users_list)
print(users)
print(len(users))

print("--------------------------------------------------------------")

users.add("Bogdan")
print(users)

print("--------------------------------------------------------------")

user="Max"

if user in users:
    users.remove(user)
print(users)

print("--------------------------------------------------------------")

print(users)
users.discard("Max")
print(users)
users.discard("Dima")
print(users)

print("--------------------------------------------------------------")

print(users)

for user in users:
    print(user)

print("--------------------------------------------------------------")

users1=users.copy()
print(users1)

print("--------------------------------------------------------------")

print(users)
users.clear()
print(users)

print("--------------------------------------------------------------")

users2 = ["Artem", "Bogdan", "Oleg"]
users3 = users1.union(users2)
print(users3)

print("--------------------------------------------------------------")

users3 = users1.intersection(users2)
print(users3)

print("--------------------------------------------------------------")

users3=users1.difference(users2)
print(users3)
users3=users1.symmetric_difference(users2)
print(users3)

print("--------------------------------------------------------------")
