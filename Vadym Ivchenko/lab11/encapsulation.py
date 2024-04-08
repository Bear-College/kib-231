class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if 0 <= age <= 120:  
            self.__age = age
        else:
            print("Неправильний вік")

    def display_info(self):
        print(f"Імя: {self.__name} \t Вік: {self.__age}")


person1 = Person("ЄГОР", 25)
person1.display_info()

person1.set_name("ІГОР")
person1.set_age(30)
person1.display_info()
