class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy = None):
        self.name = name
        self.age = age
        # self.isHappy = isHappy

        self.getData()

    def getData(self):
        print(self.name, self.age, self.isHappy)

    

cat1 = Cat('Hello', 15);