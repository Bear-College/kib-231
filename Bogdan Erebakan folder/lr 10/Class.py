class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Person: {self.name}, {self.age} years old"

class User: 
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def display_info(self):
        return f"User: {self.login}, Password: {self.password}"

class Group:
    def __init__(self, group_number, captain):
        self.group_number = group_number
        self.captain = captain

    def display_info(self):
        return f"Group: {self.group_number}, Captain: {self.captain}"

class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def display_info(self):
        return f"Subject: {self.name}, Teacher: {self.teacher}"

class Praktika:
    def __init__(self, location, num_students):
        self.location = location
        self.num_students = num_students

    def display_info(self):
        return f"Praktika: {self.location}, Students: {self.num_students}"

boda = Person("Бодя", 19)
vitya = Person("Вітґ", 20)

user_boda = User("Бодя", 456)
user_vitya = User("Вітя", "abc")

group_231 = Group("КІБ-231", "Єребакан")
group_193 = Group("КІ-193", "Щенсневич/Гурський/Івченкр/Конопацький")

subject1 = Subject("Програмування", "Атаман В.О.")
subject2 = Subject("Бази даних", "Пятін І.С.")

praktika1 = Praktika("ТОВ Неіл", 3)
praktika2 = Praktika("ПаТ Укрелектроапарат", 1)

# Вывод информации
print(boda.display_info())
print(vitya.display_info())

print(user_boda.display_info())
print(user_vitya.display_info())

print(group_231.display_info())
print(group_193.display_info())

print(subject1.display_info())
print(subject2.display_info())

print(praktika1.display_info())
print(praktika2.display_info())
