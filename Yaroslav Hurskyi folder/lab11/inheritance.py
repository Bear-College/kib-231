class Electronics:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    def brand(self):
        return self.__brand
    
    def model(self):
        return self.__model
    
    def display_info(self):
        print(f"Пристрій: {self.__brand} {self.__model}")

class System:
    def __init__(self, os):
        self.__os = os
    
    def os(self):
        return self.__os
    
    def display_info(self):
        print(f"Операційна система: {self.__os}")

class Smartphone(Electronics, System):
    def __init__(self, brand, model, os):
        Electronics.__init__(self, brand, model)
        System.__init__(self, os)

android_phone = Smartphone("Samsung", "Galaxy S21", "Android")
android_phone.display_info()

apple_phone = Smartphone("Apple", "IPhone 15 Pro", "iOS")
apple_phone.display_info()
