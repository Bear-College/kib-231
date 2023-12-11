class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if 1<age<110:
            self.__age = age
        else:
            print("Недопустимий вік")

    def display_info(self):
        print(f"Ім'я: {self.__name} \t Вік: {self.__age}")

class Employee(Person):
    def __init__(self, work):
        self.__work = work

    @property
    def work(self):
        return self.__work
    
    @work.setter
    def work(self, work):
        self.__work = work

    def display_info(self):
        print(f"Ім'я: {self.name} \t Вік: {self.age} \t Працює у: {self.__work}")

person1 = Employee('NONE')
person1.name = "Dima"
person1.age = 20
person1.work = "ЕВЕРЕСТ СК"
person1.display_info()

print("---------------------------------------------------------------------------")

class Student(Person):
    def __init__(self, education):
        self.__education = education
    
    @property
    def education(self):
        return self.__education
    
    @education.setter
    def education(self, education):
        self.__education = education

    def display_info(self):
        print(f"Ім'я: {self.name} \t Вік: {self.age} \t Навчається в: {self.__education}")

class WorkingStudent(Employee, Student):
    def __init__(self, madness):
        self.__madness = madness

    @property
    def madness(self):
        return self.__madness
    
    @madness.setter
    def madness(self, madness):
        self.__madness = madness

    def display_info(self):
        print(f"Ім'я: {self.name} \t Вік: {self.age} \n Навчається в: {self.education} \t Працює в: {self.work} \n Рівень божевілля: {self.__madness} ")
        
person2 = WorkingStudent("-") 
person2.name = "Dima"
person2.age = 20
person2.education = "ХПК"
person2.work = "ЕВЕРЕСТ СК"
person2.madness = "20%"
person2.display_info()

        