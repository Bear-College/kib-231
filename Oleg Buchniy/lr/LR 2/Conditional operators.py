import random

HealsGladiatorEnemy=100
DamageGladiatorEnemy= random.randint(1,300)

HealsGladiatorYou=100
DamageGladiatorYou= int(input("Введіть шкоду яку хочете завдати ворогу ..  "))

HealsGladiatorEnemy-=DamageGladiatorYou
HealsGladiatorYou-=DamageGladiatorEnemy
if HealsGladiatorEnemy<0:
    HealsGladiatorEnemy=0

if HealsGladiatorYou<0:
    HealsGladiatorYou=0
    
print(DamageGladiatorEnemy)
print(f"здоров'я ворожого гладіатора  : {HealsGladiatorEnemy} ")
print(f"здоров'я вашого гладіатора  : {HealsGladiatorYou}")