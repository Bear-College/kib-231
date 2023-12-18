class Employee:
    def __init__(self, name, employee_id):
        self.__name = name
        self.__employee_id = employee_id

    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Робітник: {self.__name}, ID: {self.__employee_id}")

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.__department = department

    def get_department(self):
        return self.__department

    def display_info(self):
        print(f"Менеджер: {self.get_name()}, ID: {self.get_employee_id()}, Відділ: {self.__department}")

class Engineer(Employee):
    def __init__(self, name, employee_id, specialization):
        super().__init__(name, employee_id)
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

    def display_info(self):
        print(f"Інженер: {self.get_name()}, ID: {self.get_employee_id()}, Спеціалізація: {self.__specialization}")

employee = Employee(name="Конопацький Володя", employee_id=101)
manager = Manager(name="Костюк Владік", employee_id=201, department="IT")
engineer = Engineer(name="Діма Дота2", employee_id=301, specialization="Valve DOTA2 Engineer")

employee.display_info()
manager.display_info()
engineer.display_info()
