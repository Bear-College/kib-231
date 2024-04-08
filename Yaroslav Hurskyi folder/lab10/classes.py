class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.make}\tМодель: {self.model}\tРік: {self.year}")


car1 = Vehicle("Toyota", "Camry", 2022) 
car1.display_info()
#Марка: Toyota   Модель: Camry   Рік: 2022

car2 = Vehicle("Honda", "Civic", 2023) 
car2.display_info()
# Марка: Honda    Модель: Civic   Рік: 2023


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Ємність батареї: {self.battery_capacity} kWh")


electric_car = ElectricCar("Tesla", "Model 3", 2023, 75)
electric_car.display_info()
# Марка: Tesla    Модель: Model 3 Рік: 2023
# Ємність батареї: 75 kWh


class Motorcycle:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def display_info(self):
        print(f"Марка: {self.brand}\tМодель: {self.model}\tКолір: {self.color}")


bike = Motorcycle("Harley-Davidson", "Street 750", "Чорний")
bike.display_info()
# Марка: Harley-Davidson  Модель: Street 750      Колір: Чорний

class Bicycle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def display_info(self):
        print(f"Марка: {self.brand}\tМодель: {self.model}\tТип: {self.type}")


mountain_bike = Bicycle("Trek", "Fuel EX", "Позашляхові мотоцикли")
mountain_bike.display_info()
# Марка: Trek     Модель: Fuel EX Тип: Позашляхові мотоцикли

class Boat:
    def __init__(self, name, length):
        self.name = name
        self.length = length
    def display_info(self):
        print(f"Марка: {self.name}\tДовжина: {self.length} м")


sailboat = Boat("Sailing Yacht", 40)
sailboat.display_info()
# Марка: Sailing Yacht    Довжина: 40 м