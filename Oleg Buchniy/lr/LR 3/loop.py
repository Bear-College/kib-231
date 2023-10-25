import random;

HealthGladiator1 = random.uniform(100,300)
HealthGladiator2 = random.uniform(100,300)
			
DamageGladiator1 = random.uniform(50,100)
DamageGladiator2 = random.uniform(60,90)
			
ArmorGladiator1 = random.uniform(60,70)
ArmorGladiator2 = random.uniform(50,80)

print(f"Gladiator 1: {HealthGladiator1} health , {DamageGladiator1} damage , {ArmorGladiator1} armor ")
print(f"Gladiator 2: {HealthGladiator2} health , {DamageGladiator2} damage , {ArmorGladiator2} armor \n")

#while for


Countloop=10000000
countRound = 1
DamageInRound1=0
DamageInRound2=0
while (HealthGladiator1 >0 and HealthGladiator2>0):
    print("Триває процес битви")
    for c in range(0,Countloop+1):
        if c ==3333333 or c ==6666666 or c ==9999999:
            print(".")
    DamageInRound2 = random.uniform(0,DamageGladiator2 +1) /100 *ArmorGladiator1
    HealthGladiator1 -= DamageInRound2
    DamageInRound1 = random.uniform(0,DamageGladiator1 +1) /100 *ArmorGladiator2
    HealthGladiator2 -= DamageInRound1

    if HealthGladiator1<0:
        HealthGladiator1=0

    if HealthGladiator2<0:
        HealthGladiator2=0
    print(f"\nHealth gladiator 1: {HealthGladiator1} in the {countRound} round his damage is - {DamageInRound1} ")
    print(f"Health gladiator 2: {HealthGladiator2} in the {countRound} round his damage is - {DamageInRound2} \n")

    
    countRound+=1

if (HealthGladiator1 == 0 and HealthGladiator2 == 0):
	print("RAWS")
	
elif (HealthGladiator1 ==0):
	print("GLADIATOR 2 WINS")
elif (HealthGladiator2 ==0):
	print("GLADIATOR 1 WINS")