class Book:
    def init(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")

# Створення об'єкта
book1 = Book("Майстер і Маргарита", "Михайло Булгаков")
book1.display_info()

class Car:
    def init(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")

# Створення об'єкта
car1 = Car("Toyota", "Camry")
car1.start_engine()

class Collection:
    def init(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

# Створення об'єкта
collection1 = Collection("Моя колекція")
collection1.add_item("Предмет 1")

class Student:
    def init(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} вивчає матеріал")

# Створення об'єкта
student1 = Student("Іван", 20)
student1.study()

class BankAccount:
    def init(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Поповнення рахунку на {amount} грн. Загальний баланс: {self.balance} грн.")

# Створення об'єкта
account1 = BankAccount("Ірина")
account1.deposit(1000)