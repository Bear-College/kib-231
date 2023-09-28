print ("Ok. Let's fight!")

HealsGladiator1 = 100
ArmorGladiator1 = (25* 0)/2 + (100-10)/2
DamageGladiator1= 20

HealsGladiator2 = 100
ArmorGladiator2 = (25* 0)/2 + (100-85)
DamageGladiator2= 35.2

print(f"Heals Gladiator 1 : {HealsGladiator1} , Armor: {ArmorGladiator1} , Damage : {DamageGladiator1} ")
print(f"Heals Gladiator 2 : {HealsGladiator2} , Armor: {ArmorGladiator2} , Damage : {DamageGladiator2} ")

input("Input word to start fight...")
Round1_1= HealsGladiator1+ArmorGladiator1-DamageGladiator2
Round1_2= HealsGladiator2+ArmorGladiator2-DamageGladiator1

print(f"Result round : \n Gladiator 1 has Heals and armor {Round1_1} \n Gladiator 2 has Heals and armor {Round1_2}")
