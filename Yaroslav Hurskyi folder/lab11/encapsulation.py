class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def brand(self):
        return self.brand
    
    def model(self):
        return self.model
    
    def speed(self):
        return self.speed

    def brand(self, brand):
        self.brand = brand

    def model(self, model):
        self.model = model

    def speed(self, speed):
        if 0 <= speed <= 200:
            self.speed = speed
        else:
            print("Invalid speed")


    def display_info(self):
        print(f"Марка: {self.brand} \t Модель: {self.model} \t Швидкість: {self.speed} km/h")


car1 = Car("Toyota", "Camry")
car1.display_info()

car1.brand = "Honda"
car1.model = "Civic"
car1.speed = 199
car1.display_info()

