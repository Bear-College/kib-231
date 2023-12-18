class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.make}\tМодель: {self.model}\tРік: {self.year}")


class Motorcycle:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display_info(self):
        print(f"Марка: {self.brand}\tМодель: {self.model}\tКолір: {self.color}")


class Bicycle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def display_info(self):
        print(f"Марка: {self.brand}\tМодель: {self.model}\tТип: {self.type}")


class Boat:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def display_info(self):
        print(f"Марка: {self.name}\tДовжина: {self.length} м")


# Examples of using the classes

car1 = Vehicle("Toyota", "Camry", 2022)
car1.display_info()

car2 = Vehicle("Honda", "Civic", 2023)
car2.display_info()


bike = Motorcycle("Harley-Davidson", "Street 750", "Чорний")
bike.display_info()

mountain_bike = Bicycle("Trek", "Fuel EX", "Позашляхові мотоцикли")
mountain_bike.display_info()

sailboat = Boat("Sailing Yacht", 40)
sailboat.display_info()
