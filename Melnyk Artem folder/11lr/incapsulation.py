class User:
    def init(self, username, password):
        self._username = username  # Захищений атрибут
        self.__password = password  # Приватний атрибут

    def get_username(self):
        return self._username

    def set_password(self, new_password):
        # Додаткова логіка, наприклад, перевірка безпеки паролю
        self.__password = new_password

# Створення об'єкта
user1 = User("john_doe", "secure_password")

# Звертання до захищеного та приватного атрибутів через методи
print("Username:", user1.get_username())
user1.set_password("new_secure_password")

class Worker:
    def init(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 18 <= new_age <= 65:
            self._age = new_age
        else:
            print("Неприпустимий вік для робітника.")

# Створення об'єкта
worker1 = Worker("Іван", 25)

# Використання властивостей
print("Ім'я:", worker1.name)
print("Вік:", worker1.age)

# Зміна віку через властивість
worker1.age = 30

import math

class Circle:
    def init(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

# Створення об'єкта
circle1 = Circle(5)

# Використання властивостей для отримання інформації
print("Радіус:", circle1.radius)
print("Діаметр:", circle1.diameter)
print("Площа:", circle1.area)

class Book:
    def init(self, title, author, pages):
        self._title = title
        self._author = author
        self._pages = pages

    def get_info(self):
        return f"{self._title} автора {self._author}, {self._pages} сторінок"

# Створення об'єкта
book1 = Book("Майстер і Маргарита", "Михайло Булгаков", 400)

# Звертання до захищених атрибутів через метод
print("Інформація про книгу:", book1.get_info())

class Account:
    def init(self, account_holder, balance=0):
        self._account_holder = account_holder
        self._balance = balance

    @property
    def account_holder(self):
        return self._account_holder

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Недостатньо коштів на рахунку.")

# Створення об'єкта
account1 = Account("Ірина", 1000)

# Використання властивостей та методів
print("Власник рахунку:", account1.account_holder)
print("Баланс рахунку:", account1.balance)
account1.deposit(500)
account1.withdraw(200)