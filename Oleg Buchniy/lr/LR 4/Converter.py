import random

def Instruction1():
    print("                     Вітаю у вас у грі ЖАР! \nСуть її полягає в тому, щоб в продовж гри максимально "+"\033[34m{}\033[0m".format("Охолодити")+" або "+"\033[31m{}\033[0m".format("Підсмажити")+" суперника\n"+
    "Кожного разу коли ви починаєте гру вам і вашому супернику випадково випадає завдання на "+"\033[34m{}\033[0m".format("Охолодження")+" або "+"\033[31m{}\033[0m".format("Підсмаження") +"\n"
    +"Задача "+"\033[31m{}\033[0m".format("підсмаження")+" - максимально завдати шкоду з "+"\033[31m{}\033[0m".format("найвищою")+" температурою за хід \n"
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

ChouseTask = int(input("\nОберіть яку шкоду будете завдавати супернику: \n 1 - "+"\033[34m{}\033[0m".format("Охолодження")+" \n 2 - "+"\033[31m{}\033[0m".format("Підсмаження")+" \n"))
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


print(f"Ваша задача - {YourTask}"+" \n \n \n \n \n \n \n ")
print(f"Задача суперника - {EnemyTaks} \n")

YourDamage=int(input("Введіть шкоду яку хочете завдати супернику У цельсіях (Tемпературу можна не писати з мінусом '-',\nякщо у вас завдання на ("+"\033[34m{}\033[0m".format("oхолодження")+"): "))
if EnemyTaks=="\033[31m{}\033[0m".format("Підсмаження"):
    EnemyDamage=random.randint(32,1000)
else: 
    EnemyDamage=random.randint(32,1000) 
print("")
if YourDamage>0 and YourTask=="\033[34m{}\033[0m".format("Охолодження"):
    YourDamage=-YourDamage
    print(f"Суперник наніс вам : "+f"\033[31m{EnemyDamage}\033[0m".format() +" фарангейт або " f"\033[31m{FahrenheitToCelsius(EnemyDamage)}\033[0m".format() +"  целсій")
    print("Ви нанесли ворогу: "+f"\033[34m{YourDamage}\033[0m".format() +" цельсій або " +f"\033[34m{CelsiusToFahrenheit(YourDamage)}\033[0m".format() +" фаренгейт") 
    YourDamage=-YourDamage

elif EnemyDamage>0 and EnemyTaks=="\033[34m{}\033[0m".format("Охолодження"):
    EnemyDamage=-EnemyDamage
    print(f"Суперник наніс вам : "+f"\033[34m{EnemyDamage}\033[0m".format() +" фарангейт або " +f"\033[34m{FahrenheitToCelsius(EnemyDamage)}\033[0m".format() +"  целсій")
    print("Ви нанесли ворогу: "+f"\033[31m{YourDamage}\033[0m".format() +" цельсій або " +f"\033[31m{CelsiusToFahrenheit(YourDamage)}\033[0m".format() +" фаренгейт") 
    EnemyDamage=-EnemyDamage

elif YourDamage<0 and YourTask=="\033[34m{}\033[0m".format("Охолодження"):
    print(f"Суперник наніс вам : "+f"\033[31m{EnemyDamage}\033[0m".format() +" фарангейт або " f"\033[31m{FahrenheitToCelsius(EnemyDamage)}\033[0m".format() +"  целсій")
    print("Ви нанесли ворогу: "+f"\033[34m{YourDamage}\033[0m".format() +" цельсій або " +f"\033[34m{CelsiusToFahrenheit(YourDamage)}\033[0m".format() +" фаренгейт") 
    YourDamage=-YourDamage

CelsiusToFahrenheit(EnemyDamage)

if (YourDamage == EnemyDamage):
	print("\nНічія!")
	
elif (YourDamage >= EnemyDamage):
	print("\nВітаю, ви перемогли !!")
elif (YourDamage <= EnemyDamage):
	print("\nПоразка!! Ворог переіг")
