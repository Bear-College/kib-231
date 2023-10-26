import random

def Instruction1():
    print("\n                     Вітаю у вас у грі ЖАР! \nСуть її полягає в тому, щоб в продовж гри максимально "+"\033[34m{}\033[0m".format("Охолодити")+" або "+"\033[31m{}\033[0m".format("Підсмажити")+" суперника\n"+
    "Кожного разу коли ви починаєте гру вам і вашому супернику випадково випадає завдання на "+"\033[34m{}\033[0m".format("Охолодження")+" або "+"\033[31m{}\033[0m".format("Підсмаження") +"\n"
    +"\nЗадача "+"\033[31m{}\033[0m".format("підсмаження")+" - максимально завдати шкоду з "+"\033[31m{}\033[0m".format("найвищою")+" температурою за хід \n"
    +"Задача "+"\033[34m{}\033[0m".format("охолодження")+" - максимально завдати шкоду з "+"\033[34m{}\033[0m".format("найнищою")+" температурою за хід \n"
    +"Задачі у вас і суперника виконується по різному \n"
    +"Відрізняєтся лише тим що ви наносите шкоду в градусах Целсія а ваш суперник у Фаренгейта\n")

def FahrenheitToCelsius(Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5/9
    return Celsius

def CelsiusToFahrenheit(Celsius):
    Fahrenheit = (Celsius * 9/5) + 32
    return Fahrenheit

Instruction1()

ChouseTask = int(input("\nОберіть яку шкоду будете завдавати супернику: \n 1 - "+"\033[34m{}\033[0m".format("Охолодження")+" \n 2 - "+"\033[31m{}\033[0m".format("Підсмаження")+" \n \n"))
YourTask=0
EnemyTaks=0

if ChouseTask==1:
    YourTask="\033[34m{}\033[0m".format("Охолодження")
    EnemyTaks="\033[31m{}\033[0m".format("Підсмаження")
elif ChouseTask==2:
    YourTask="\033[31m{}\033[0m".format("Підсмаження")
    EnemyTaks="\033[34m{}\033[0m".format("Охолодження")
else:
    print("Неправильно введені дані. Ваша шкода - "+"\033[34m{}\033[0m".format("Охолодження"))
    YourTask="\033[34m{}\033[0m".format("Охолодження")
    EnemyTaks="\033[31m{}\033[0m".format("Підсмаження")

WordAfterRound=""
WordTask=""
CounterTask=0
SumYourDamage=0
SumEnemyDamage=0 

while (WordAfterRound!="stop" and WordAfterRound!="Stop" and WordAfterRound!="STOP" and WordAfterRound!="sTOP" and WordAfterRound!="S" and WordAfterRound!="s") :
    
    print(f"Ваша задача - {YourTask}"+" \n \n \n \n \n \n \n ")
    print(f"Задача суперника - {EnemyTaks} \n")

    YourDamage=int(input("Введіть шкоду яку хочете завдати супернику У цельсіях (Tемпературу можна не писати з мінусом '-',\nякщо у вас завдання на ("+"\033[34m{}\033[0m".format("oхолодження")+"): "))
    if EnemyTaks=="\033[31m{}\033[0m".format("Підсмаження"):
        EnemyDamage=random.randint(32,1000)
    else: 
        EnemyDamage=random.randint(32,1000) 
        
    print("")
    

    if YourDamage>0 and YourTask=="\033[34m{}\033[0m".format("Охолодження"):
        SumYourDamage+=YourDamage
        SumEnemyDamage+=EnemyDamage

        SumYourDamage=-SumYourDamage
        
        print(f"Суперник наніс вам : "+f"\033[31m{SumEnemyDamage}\033[0m".format() +" фарангейт або " f"\033[31m{FahrenheitToCelsius(SumEnemyDamage)}\033[0m".format() +"  целсій")
        print("Ви нанесли ворогу: "+f"\033[34m{SumYourDamage}\033[0m".format() +" цельсій або " +f"\033[34m{CelsiusToFahrenheit(SumYourDamage)}\033[0m".format() +" фаренгейт") 
        
        SumYourDamage=-SumYourDamage

    elif EnemyDamage>0 and EnemyTaks=="\033[34m{}\033[0m".format("Охолодження"):
        SumYourDamage+=YourDamage
        SumEnemyDamage+=EnemyDamage

        SumEnemyDamage=-SumEnemyDamage
        print(f"Суперник наніс вам : "+f"\033[34m{SumEnemyDamage}\033[0m".format() +" фарангейт або " +f"\033[34m{FahrenheitToCelsius(SumEnemyDamage)}\033[0m".format() +"  целсій")
        print("Ви нанесли ворогу: "+f"\033[31m{SumYourDamage}\033[0m".format() +" цельсій або " +f"\033[31m{CelsiusToFahrenheit(SumYourDamage)}\033[0m".format() +" фаренгейт") 

        SumEnemyDamage=-SumEnemyDamage

    elif YourDamage<0 and YourTask=="\033[34m{}\033[0m".format("Охолодження"):
        YourDamage=-YourDamage
        SumYourDamage+=YourDamage
        SumEnemyDamage+=EnemyDamage

        SumYourDamage=-SumYourDamage
        print(f"Суперник наніс вам : "+f"\033[31m{SumEnemyDamage}\033[0m".format() +" фарангейт або " f"\033[31m{FahrenheitToCelsius(SumEnemyDamage)}\033[0m".format() +"  целсій")
        print("Ви нанесли ворогу: "+f"\033[34m{SumYourDamage}\033[0m".format() +" цельсій або " +f"\033[34m{CelsiusToFahrenheit(SumYourDamage)}\033[0m".format() +" фаренгейт") 
        
        SumYourDamage=-SumYourDamage

    WordAfterRound=input("\nПродовжуєм? c/s (continue/stop) : ")
    
    # if WordAfterRound!="c" and WordAfterRound!="C" and WordAfterRound!="continue" and WordAfterRound!="Continue" and WordAfterRound!="CONTINUE" :
    #     print("Неправильно введені дані. \n")
    

CelsiusToFahrenheit(SumEnemyDamage)

if (SumYourDamage == SumEnemyDamage):
	print("\nНічія")
	
elif (SumYourDamage >= SumEnemyDamage):
	print("\nВітаю, ви перемогли !!")
elif (SumYourDamage <= SumEnemyDamage):
	print("\nПоразка!! Ворог переіг")