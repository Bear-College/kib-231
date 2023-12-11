class Animal:
    def speak(self):
        return "Звук тварини"

class Dog(Animal):
    def bark(self):
        return "Гав-гав"

# Створення об'єктів
animal = Animal()
dog = Dog()

# Використання успадкованих методів
print(animal.speak())  # "Звук тварини"
print(dog.speak())     # "Звук тварини"
print(dog.bark())      # "Гав-гав"

class Shape:
    def area(self):
        return "Площа фігури"

class Square(Shape):
    def init(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Створення об'єктів
shape = Shape()
square = Square(5)

# Використання успадкованих методів
print(shape.area())   # "Площа фігури"
print(square.area())  # 25

class Engine:
    def start(self):
        return "Двигун запущено"

class ElectricDevice:
    def charge(self):
        return "Пристрій заряджено"

class ElectricCar(Engine, ElectricDevice):
    pass

# Створення об'єкта
electric_car = ElectricCar()

# Використання методів від обох батьківських класів
print(electric_car.start())   # "Двигун запущено"
print(electric_car.charge())  # "Пристрій заряджено"

class Person:
    def init(self, name):
        self.name = name

class Job:
    def init(self, title):
        self.title = title

class Employee(Person, Job):
    def init(self, name, title, salary):
        Person.init(self, name)
        Job.init(self, title)
        self.salary = salary

# Створення об'єкта
employee = Employee("Іван", "Програміст", 50000)

# Використання атрибутів від обох батьківських класів
print(employee.name)   # "Іван"
print(employee.title)  # "Програміст"
print(employee.salary) # 50000

class Shape:
    def area(self):
        return "Площа фігури"

class Color:
    def color_info(self):
        return "Колір фігури"

class ColoredShape(Shape, Color):
    def init(self, color):
        self.color = color

    def area(self):
        return "Перевизначена площа фігури"

# Створення об'єкта
colored_shape = ColoredShape("червоний")

# Використання методів та атрибутів від обох батьківських класів
print(colored_shape.area())       # "Перевизначена площа фігури"
print(colored_shape.color_info()) # "Колір фігури"