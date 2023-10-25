class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Ім'я : {self.name} \t Вік: {self.age}")

print("---------------------------------------------------------------------------")

dima = Person("Дмитро", 20)
dima.display_person()

pasha = Person("Павло", 22)
pasha.display_person()

print("---------------------------------------------------------------------------")

class User: 
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def display_user(self):
        print(f"Логін: {self.login} \t  Пароль: {self.password}")

user_dima = User("Дмитро", 123)
user_dima.display_user()

user_pasha = User("Павло", "abc")
user_pasha.display_user()

print("---------------------------------------------------------------------------")

class Group:
    def __init__(self, nomer, starosta):
        self.nomer = nomer
        self.starosta = starosta
    def display_group(self):
        print(f"Номер групи: {self.nomer} \t  Староста: {self.starosta}")

group_231 = Group("КІБ-231", "Єребакан")
group_231.display_group()

group_193 = Group("КІ-193", "Сапожнік/Возінський/Конопацький/Лахман")
group_193.display_group()
        
print("---------------------------------------------------------------------------")

class Subject:
    def __init__(self, nazva, teacher):
        self.nazva = nazva
        self.teacher = teacher
    def display_subject(self):
        print(f"Назва предмету: {self.nazva} \t  Викладач: {self.teacher}")
    
subject1 = Subject("Програмування", "Атаман В.О.")
subject1.display_subject()

subject2 = Subject("Бази даних","Пятін І.С.")
subject2.display_subject()

print("---------------------------------------------------------------------------")

class Praktika:
    def __init__(self, place, kil):
        self.place = place
        self.kil = kil
    def display_prktika(self):
        print(f"База практики: {self.place} \t  Кількість студентів: {self.kil}")

praktika1 = Praktika("ТОВ ОТМ ГРУП",3)
praktika1.display_prktika()

praktika2 = Praktika("ПРаТ Хмельпиво",1)
praktika2.display_prktika()

print("---------------------------------------------------------------------------")