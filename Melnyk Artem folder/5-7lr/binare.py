import pickle

FILENAME = "C:\Users\User\Desktop\Melnyk Artem\user.dat"

name = "Alex"
age = 21

with open(FILENAME,"wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FILENAME,"rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Ім'я",name, "\tВік:",age)