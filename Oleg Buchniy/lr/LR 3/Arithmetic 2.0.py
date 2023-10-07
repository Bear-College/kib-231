import random;

#def RandomHeal (HealsGladiator):
#   return HealsGladiator == random.randint(200,300)
#def RandomSpecification(Specification):
#    return Specification== random.randint(1,3)
def out_blue(text):
    print("\033[34m{}\033[0m".format(text))
def out_red(text):
    print("\033[31m{}\033[0m".format(text))
def out_yellow(text):
    print("\033[33m{}\033[0m".format(text))
def draw_shieldmaster():
    out_red("                            ————————        \n"+
            "                          /   ————   \       \n"+
            "                         /   |    |   \       \n"+
            "                         \   |    |   /        \n"+
            "                     "+"\033[33m{}\033[31m".format("/|")+"   \   \__/   /   \      \n"
            "                     "+"\033[33m{}\033[31m".format("/")+"      ————————      \      \n"
            "                    "+"\033[33m{}\033[31m".format("/")+"                      \      \n"
            "                   "+"\033[33m{}\033[31m".format("/")+"                       \/      ")
def draw_masters():
    out_yellow("               ————————                "+"\033[34m{}\033[33m".format("   ————————        ")+"\n"+
               "             /    /\    \              "+"\033[34m{}\033[33m".format(" /   |  |   \      ")+"\n"+
               "            /    |  |    \  "+"\033[34m{}\033[33m".format("/__ __ __  /   _|  |_   \     ")+"\n"+
               "            \   _|__|_   /  "+"\033[34m{}\033[33m".format("\          \   \    /   /     ")+"\n"+
               "             \    ||    /              "+"\033[34m{}\033[33m".format(" \   \::/   /      ")+"\n"+
               "               ————————                "+"\033[34m{}\033[0m".format ("   ————————        ")+"\n") 
def Instruction():
    print("\n Гра складається з одного раунду \nза який ви повинні якнайефективніше завдати шкоди свому супернику \nшляхом вибору найефективнішого удару для досягнення цієї задачі \nВсьоого їх існує 3 вида, як і спеціалізацій(про них трохи згодом)\nПри виборі удару ваша базова шкода супернику може зменшитись або збільшитись \n в залежності від того яка у вас спеціалізація \nВмикайте голову!!! ")
    print("\nКожного раунду гравцю випадає випадкова спеціалізація ")
    print("Вона існує трьох видів: \n \n1-"+"\033[33m{}\033[0m".format("Мечники")+", ефеетивно наносять - "+"\033[33m{}\033[0m".format("(Ріжучий удар)")+"\n2-"+"\033[34m{}\033[0m".format("Копійники")+", ефективно наносять - "+"\033[34m{}\033[0m".format("(Колючий удар)")+"\n3-"+"\033[31m{}\033[0m".format("Щитоносці")+", ефективно наносять ""\033[31m{}\033[0m".format("(Глухо-роздроблювальний удар) \n"))
    
    print("В кожної їз цих спеціалізацій є свої переваги та недоліки: \n")
    print("\033[33m{}\033[0m".format("Мечники")+" мають перевагу над "+"\033[31m{}\033[0m".format("Щитоносцями")+" але програють "+"\033[34m{}\033[0m".format("Копійникам"))
    print("\033[34m{}\033[0m".format("Копійники")+" мають перевагу над "+"\033[33m{}\033[0m".format("Мечниками")+" але але надзичайно не ефективні проти "+"\033[31m{}\033[0m".format("Щитоносців"))
    print("\033[31m{}\033[0m".format("Щитоносці")+" мають перевагу над "+"\033[34m{}\033[0m".format("Копійниками")+" але програють "+"\033[33m{}\033[0m".format("Мечникам"))
    draw_shieldmaster()
    draw_masters()

Instructionskip=input("\n                                Вітаємо вас у грі Гладіатори \n Наполегливо рекомендуєм вам максимально розтягнути вікно вашого засобу виводу для комфортної гри\n                           Бажаєте пропустити інструкцію до гри? y/n \n")
if Instructionskip=="Yes" or Instructionskip=="y" or Instructionskip=="yes" or Instructionskip=="YES":
    print("\n")
elif Instructionskip=="No" or Instructionskip=="n" or Instructionskip=="no" or Instructionskip=="NO":
    Instruction()
else:
    print("Неправильно введені дані. Провсяк випадок ми покажем вам інструкцію")
    Instruction()

HealsGladiatorEnemy=1000
SpecificationGladiatorEnemy = random.randint(1,3)
DamageGladiatorEnemy= 20

CrusialPow=2

HealsGladiatorYou = 1000
SpecificationGladiatorYou = random.randint(1,3)
DamageGladiatorYou= 20

if SpecificationGladiatorEnemy==1:
    SpecificationGladiatorEnemy="\033[33m{}\033[0m".format("Meчник")
elif SpecificationGladiatorEnemy==2:
    SpecificationGladiatorEnemy="\033[34m{}\033[0m".format("Копійник")
elif SpecificationGladiatorEnemy==3:    
    SpecificationGladiatorEnemy="\033[31m{}\033[0m".format("Щитоносець")

if SpecificationGladiatorYou==1:
    SpecificationGladiatorYou="\033[33m{}\033[0m".format("Meчник")
elif SpecificationGladiatorYou==2:
    SpecificationGladiatorYou="\033[34m{}\033[0m".format("Копійник")
elif SpecificationGladiatorYou==3:    
    SpecificationGladiatorYou="\033[31m{}\033[0m".format("Щитоносець")

RandPosleBoyaKulakamiNeMashut=random.randint(1,3)
if RandPosleBoyaKulakamiNeMashut==1:
    PosleBoyaKulakamiNeMashut="\nРаунд завершенно! Гладіатори, відпочиньте і готуйтеся до наступного бою! \n"
elif RandPosleBoyaKulakamiNeMashut==2:
    PosleBoyaKulakamiNeMashut="\nЧас на відпочинок, гладіатори! Ви показали справжній майстер клас \n"
elif RandPosleBoyaKulakamiNeMashut==3:
    PosleBoyaKulakamiNeMashut="\nВаші зусилля гідно відзначенні, гладіатори! Ви бились до останнього, GG \n"
#instruction

BattleCry=input("\n Якщо все зрозуміло тоді почнемо \nВведіть бойове гасло для початку битви \n")
print(BattleCry+"!!! \n")


print(f"HP ворога: {HealsGladiatorEnemy}. Базова шкода ворога: {DamageGladiatorEnemy} . Спеціалізація ворога : {SpecificationGladiatorEnemy} \n \n \n \n \n \n \n \n \n \n ")
print(f"HP гравця: {HealsGladiatorYou}. Ваша базова шкода: {DamageGladiatorYou} . Ваша спеціалізація: {SpecificationGladiatorYou} \n")

YourTurn=int(input("Який тип удару ви хочете завдати ? \n "+"\033[33m{}\033[0m".format("Ріжучий - 1 ")+"\033[34m{}\033[0m".format("\n Колющий удар - 2")+"\033[31m{}\033[0m".format("\n Ударно-роздроблювальний удар - 3")+"\n Перейти до інструкції - 4 (Раунд завершиться без вашого втручання ,без зміни ефективності шкоди!!! ) \n"))
EnemyTurn=random.randint(1,3)

if EnemyTurn==1 and SpecificationGladiatorEnemy=="\033[33m{}\033[0m".format("Meчник") or EnemyTurn==2 and SpecificationGladiatorEnemy=="\033[34m{}\033[0m".format("Копійник") or EnemyTurn==3 and SpecificationGladiatorEnemy=="\033[31m{}\033[0m".format("Щитоносець") :
    DamageGladiatorEnemy*=CrusialPow
elif EnemyTurn==3 and SpecificationGladiatorEnemy=="\033[34m{}\033[0m".format("Копійник")  or EnemyTurn==3 and SpecificationGladiatorEnemy=="\033[33m{}\033[0m".format("Meчник") or EnemyTurn==2 and SpecificationGladiatorEnemy=="\033[31m{}\033[0m".format("Щитоносець") :
    DamageGladiatorEnemy%=DamageGladiatorEnemy
elif EnemyTurn==1 and SpecificationGladiatorEnemy=="\033[34m{}\033[0m".format("Копійник")  or EnemyTurn==2 and SpecificationGladiatorEnemy=="\033[33m{}\033[0m".format("Meчник") or EnemyTurn==1 and SpecificationGladiatorEnemy=="\033[31m{}\033[0m".format("Щитоносець") :
    DamageGladiatorEnemy+=DamageGladiatorEnemy

if YourTurn==1 and SpecificationGladiatorYou=="\033[33m{}\033[0m".format("Meчник") or YourTurn==2 and SpecificationGladiatorYou=="\033[34m{}\033[0m".format("Копійник") or YourTurn==3 and SpecificationGladiatorYou=="\033[31m{}\033[0m".format("Щитоносець") :
    DamageGladiatorYou*=CrusialPow
elif YourTurn==3 and SpecificationGladiatorYou=="\033[34m{}\033[0m".format("Копійник")  or YourTurn==3 and SpecificationGladiatorYou=="\033[33m{}\033[0m".format("Meчник") or YourTurn==2 and SpecificationGladiatorYou=="\033[31m{}\033[0m".format("Щитоносець") :
    DamageGladiatorYou%=DamageGladiatorYou
elif YourTurn==1 and SpecificationGladiatorYou=="\033[34m{}\033[0m".format("Копійник")  or YourTurn==2 and SpecificationGladiatorYou=="\033[33m{}\033[0m".format("Meчник") or YourTurn==1 and SpecificationGladiatorYou=="\033[31m{}\033[0m".format("Щитоносець") :
    DamageGladiatorYou+=DamageGladiatorYou
elif YourTurn==4:
    Instruction()

if SpecificationGladiatorEnemy=="\033[33m{}\033[0m".format("Meчник") and SpecificationGladiatorYou=="\033[31m{}\033[0m".format("Щитоносець") or SpecificationGladiatorEnemy=="\033[31m{}\033[0m".format("Щитоносець") and SpecificationGladiatorYou=="\033[34m{}\033[0m".format("Копійник") or SpecificationGladiatorEnemy=="\033[34m{}\033[0m".format("Копійник") and SpecificationGladiatorYou=="\033[33m{}\033[0m".format("Meчник"):
    DamageGladiatorEnemy**=CrusialPow
    DamageGladiatorYou+=CrusialPow

    HealsGladiatorEnemy-=DamageGladiatorYou
    HealsGladiatorYou-=DamageGladiatorEnemy

    if HealsGladiatorEnemy<0:
        HealsGladiatorEnemy=0

    if HealsGladiatorYou<0:
        HealsGladiatorYou=0
    print(f"\nПодряпина! Удар майже не зачепив супернка! {PosleBoyaKulakamiNeMashut} \n Результати раунду : \n Шкода нанесена гравцем - {DamageGladiatorYou} \n Здоров'я гравця - {HealsGladiatorYou} \n Шкода нанесена воргом - {DamageGladiatorEnemy} \n Здоров'я ворога - {HealsGladiatorEnemy}\n")
elif SpecificationGladiatorYou=="\033[33m{}\033[0m".format("Meчник") and SpecificationGladiatorEnemy=="\033[31m{}\033[0m".format("Щитоносець") or SpecificationGladiatorYou=="\033[31m{}\033[0m".format("Щитоносець") and SpecificationGladiatorEnemy=="\033[34m{}\033[0m".format("Копійник") or SpecificationGladiatorYou=="\033[34m{}\033[0m".format("Копійник") and SpecificationGladiatorEnemy=="\033[33m{}\033[0m".format("Meчник") :
    DamageGladiatorEnemy+=CrusialPow
    DamageGladiatorYou**=CrusialPow

    HealsGladiatorEnemy-=DamageGladiatorYou
    HealsGladiatorYou-=DamageGladiatorEnemy

    if HealsGladiatorEnemy<0:
        HealsGladiatorEnemy=0

    if HealsGladiatorYou<0:
        HealsGladiatorYou=0
    print(f"\nКРИТИЧНА шкода супернку! Так тримати {PosleBoyaKulakamiNeMashut} \n Результати раунду : \n Шкода нанесена гравцем - {DamageGladiatorYou} \n Здоров'я гравця - {HealsGladiatorYou} \n Шкода нанесена воргом - {DamageGladiatorEnemy} \n Здоров'я ворога - {HealsGladiatorEnemy}\n")
elif SpecificationGladiatorEnemy==SpecificationGladiatorYou:
    DamageGladiatorEnemy*=CrusialPow
    DamageGladiatorYou*=CrusialPow

    HealsGladiatorEnemy-=DamageGladiatorYou
    HealsGladiatorYou-=DamageGladiatorEnemy

    if HealsGladiatorEnemy<0:
        HealsGladiatorEnemy=0

    if HealsGladiatorYou<0:
        HealsGladiatorYou=0
    print(f"\nНепогано! Виглядає наче суперники билися на рівних {PosleBoyaKulakamiNeMashut} \n Результати раунду : \n Шкода нанесена гравцем - {DamageGladiatorYou} \n Здоров'я гравця - {HealsGladiatorYou} \n Шкода нанесена воргом - {DamageGladiatorEnemy} \n Здоров'я ворога - {HealsGladiatorEnemy} \n")







    