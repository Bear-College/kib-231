class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if 1<age<110:
            self.__age = age
        else:
            print("Недопустимий вік")
    
    @property
    def get_name(self):
        return self.__name
    
    def display_info(self):
        print(f"Ім'я: {self.__name} \t Вік: {self.__age}")

dima = Person("dima")
dima.display_info()
dima.age = -10
dima.display_info()
dima.age = 20
dima.display_info()

print("---------------------------------------------------------------------------")

class User:
    def __init__(self, login, password):
        self.__login = login
        self.__password = password
    
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, login):
        if login != "admin":
            self.__login = login
        else:
            print("Змініть логін")
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        if password != "admin":
            self.__password = password
        else: 
            print("Змініть пароль")

    def display_user(self):
        print(f"Логін: {self.__login} \t Пароль: {self.__password}")

user1 = User("user1", "user1")
user1.display_user()
user1.login = "admin"
user1.password = "admin"
user1.display_user()
user1.login = "dima"
user1.password = 12345678
user1.display_user()