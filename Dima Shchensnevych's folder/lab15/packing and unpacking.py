users = [
    ("Bob", 40, "Apple"),
    ("Sam", 35, "Google"),
    ("Tom", 31, "Microsoft")
]

for name, age, company in users:
    print(f"{name} \t {age} \t {company}")

print("--------------------------------------------------")

users = ["Bob","Sam", "Tom"]
for index, name in enumerate(users):
    print(f"{index} {name}")

print("--------------------------------------------------")

user = ["Tom", 31, "Microsoft"]
name, _, company = user
print(name)
print(company)
print(_)

print("--------------------------------------------------")

first, *middle, last = [1,2,3,4,5,6,7,8,9,10] 
print(first)
print(last)
print(middle)

print("--------------------------------------------------")

n1 = [1,2,3]
n2 = (4,5,6)
n3 = [*n1,*n2]
print(n3)

print("--------------------------------------------------")

dic1 = {"red":"червоний", "green":"зелений", "blue":"синій"}
dic2 = {"white":"білий", "black":"чорний"}
dic3 = {**dic1, **dic2 }
print(dic3)