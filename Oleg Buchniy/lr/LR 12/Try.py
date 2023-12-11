import random

class GladiatorDamageException(Exception):
    def __init__(self, damage, mindamage, maxdamage):
        self.damage = damage
        self.mindamage = mindamage
        self.maxdamage = maxdamage
 
    def __str__(self):
        return f"Invalid значення: {self.damage}. " \
               f"Шкода повинна бути від {self.mindamage} до {self.maxdamage}"

class GladiatorHealthException(Exception):
    def __init__(self, health,minhealth,maxhealth):
        self.health = health
        self.minhealth = minhealth
        self.maxhealth = maxhealth
 
    def __str__(self):
        return f"Invalid значення: {self.health}. " \
               f"Здоров'я повинно бути від {self.minhealth} до {self.maxhealth}"
 
class Gladiator:
    def __init__(self, name, healthgladiator, damagegladiator):
        self.__name = name  
        mindamage, maxdamage = 1, 110                 ##
        minhealth,maxhealth= 1,1000

        if mindamage < damagegladiator < maxdamage:   ##
            self.__damagegladiator = damagegladiator
        else:                       
            raise GladiatorDamageException(damagegladiator, mindamage, maxdamage)
        
        if minhealth < healthgladiator < maxhealth:
            self.__healthgladiator = healthgladiator
        else:
            raise GladiatorHealthException(healthgladiator, minhealth, maxhealth)

    def display_info(self):
        print(f"Name: {self.__name} Health: {self.__healthgladiator} Damage: {self.__damagegladiator}")

try: 
    YourGladiatorDamage=int(input("Введіть шкоду вашого гладіатора "))
    YourGladiatorHealth=int(input("Введіть здоров'я вашого гладіатора "))
    YourGladiatorName=input("Введіть ім'я вашого гладіатора ")
except ValueError as e:
    print("Помилка значень: "+ e)

try:
    You = Gladiator(YourGladiatorName, YourGladiatorHealth, YourGladiatorDamage)
    You.display_info() 

    bob = Gladiator("Enemy Bob", random.randint(1,1000), random.randint(1,100))
    bob.display_info()
except GladiatorDamageException as e:
    print(e) 
except GladiatorHealthException as e:
    print(e) 
finally:
    print("the End ")
