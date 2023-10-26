
import logging
import csv
import pickle

from colorama import Fore,Back,Style
from colorama import init
init(autoreset=True)

#Відкриття файлу.
# Виконання операцій (зчитування або запис).
#Закриття файлу.
FinallyQuestion=input("\033[32m{}\033[0m".format("\nВиконати умову завдання чи бути щасливим? :) \n"))
if(FinallyQuestion=="бути щасливим" or FinallyQuestion=="Бути щасливим" or FinallyQuestion=="бути Щасливим" or FinallyQuestion=="БУТИ ЩАСЛИВИМ" or FinallyQuestion=="Щасливим" or FinallyQuestion=="ЩАСЛИВИМ" or FinallyQuestion=="щасливим" or FinallyQuestion=="бути" or FinallyQuestion=="БУТИ щасливим" or FinallyQuestion=="Бутищасливим"or FinallyQuestion=="be happy"or FinallyQuestion=="Be happy"or FinallyQuestion=="behappy"or FinallyQuestion=="be happy "or FinallyQuestion=="BE HAPPY"or FinallyQuestion=="h" or FinallyQuestion=="щ"):
    
    print(Fore.BLUE+'1 - Текстовий файл')
    print(Fore.YELLOW+'2 - CSV файл')
    print(Fore.RED+'3 - Бінарний файл')
    
    TrueChoise=int(input())
    
    Questions = list([Fore.GREEN+"Що таке декоратор?", Fore.MAGENTA+"Що таке замикання?", Fore.GREEN+"Що таке PyPi?", Fore.MAGENTA+"U2FtYnlha2FuZSB0b3RvIHNpa2F5IG5vIHlvdXpoaW8gbyBtYWUgb25vbm8gbyBraWthIHMgZGVrYXJl ?"])
    if(TrueChoise==1):

        logging.basicConfig(level=logging.DEBUG, filename='TrueTask.txt', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                            encoding = 'utf-8', filemode='w')



        messages = list()
        init(autoreset=False)

        for i in range(4):
            print("\n"+Questions[i])
            message = input(Fore.BLUE+"Ваша відповідь на "+str(i+1)+" запитання: ")
            messages.append(message)
            print("Так і запишем")
        init(autoreset=True)    

        logging.debug(messages)
        logging.info('Хай')
        logging.warning('Щастить')
        

    if(TrueChoise==2):

        logging.basicConfig(level=logging.DEBUG, filename='TrueTask.csv', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                            encoding = 'utf-8', filemode='w')



        messages = list()
        init(autoreset=False)

        for i in range(4):
            print("\n"+Questions[i])
            message = input(Fore.YELLOW+"Ваша відповідь на "+str(i+1)+" запитання: ")
            messages.append(message)
            print("Так і запишем")
        init(autoreset=True)    

        logging.debug(messages)
        logging.error('Thanks')
        logging.critical('For your time')
    
    if(TrueChoise==3):

        logging.basicConfig(level=logging.DEBUG, filename='TrueTask.dat', format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]', datefmt='%d/%m/%Y %I:%M:%S',
                            encoding = 'utf-8', filemode='w')



        messages = list()
        init(autoreset=False)

        for i in range(4):
            print("\n"+Questions[i])
            message = input(Fore.RED+"Ваша відповідь на "+str(i+1)+" запитання: ")
            messages.append(message)
            print("Так і запишем")
        init(autoreset=True)    

        logging.error('Your')
        logging.debug(messages)
        logging.critical('Answer')    

else:
    print("................... :_: \n")
    print(Fore.BLUE+'1 - Текстовий файл')
    print(Fore.YELLOW+'2 - CSV файл')
    print(Fore.RED+'3 - Бінарний файл')
    
    DisChoise=int(input())
    
    if(DisChoise==1):
        TaskFile = "task.txt"
        messages = list()

        for i in range(4):
            message = input(Fore.BLUE+"Вашa "+str(i+1)+" строка: ")
            messages.append(message +"\n")
            print("Так і запишем") 

        with open(TaskFile, "a") as file:
            for message in messages:
                file.write(message)
 
        
        print("Your messages: ")
        with open(TaskFile, "r") as file:
            for message in file:
                print(message, end="")

    if(DisChoise==2):

        TaskFile = "task.csv"

        ChoiseFileMod=int(input("Сворити файл - 1 \nДописати файл - 2 \n"))
        
        if(ChoiseFileMod==1):

            Heroes= [
                [Fore.BLUE+"Ім'я героя   ",Fore.GREEN+"           Суперздібеість           ",Fore.RED+"Побічні ефекти"],
                ["One punch man","Вигравати будь-який бій одним ударом","Облисіння. Суперсила не діє на комарів"],
                ["Род          ","Бог                                 ","Бог але тільки в себе в голові "],
                ["Mello        ","Здатність літати                    ","Тільки на 10 см від землі"]
            ]

            for i in range(1000):
                person = list()

                HeroName=input("Ім'я вашого супер героя: ")
                EndIndexName=len("One punch man")
                if(len(HeroName)<EndIndexName):
                    person.append(HeroName.ljust(EndIndexName))
                else:
                    person.append(HeroName[:EndIndexName])

                HeroSuperPower=input("Його суперздібність: ")
                EndIndexPower=len("Вигравати будь-який бій одним ударом")
                person.append(HeroSuperPower[:EndIndexPower])

                person.append(input("Бобічні ефекти: "))
                # добавление вложенного списка
                Heroes.append(person)
                #Heroes[i-1]= person
                BreakQuestion=input("Продовжити? y/n ")
                if BreakQuestion=="No" or BreakQuestion=="n" or BreakQuestion=="no" or BreakQuestion=="NO":
                    break

            with open(TaskFile, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(Heroes)
        
        if(ChoiseFileMod==2):
            
            # Heroes=[

            # ]
            # for i in range(1000):
            #     person = list()
            #     person.append(input("Ім'я вашого супер героя: "))
            #     person.append(input("Його суперздібність: "))
            #     person.append(input("Бобічні ефекти: "))
     # #ШО ЗА ХУЙНЯ ХУЛІ ВОНО НЕ ПРАЦЮЄ?????????????????? ВОНИ Ж ОДНАКОВІ!!!!!!!!!   добавление вложенного списка
            #     Heroes.append(person)
            #     #Heroes[i-1]= person
            #     BreakQuestion=input("Продовжити? y/n ")
            #     if BreakQuestion=="No" or BreakQuestion=="n" or BreakQuestion=="no" or BreakQuestion=="NO":
            #         break
            
            # with open(TaskFile, "w", newline="") as file:
            #     #NewHeroes = ["Sam", 31, "fbfgnn"]
            #     writer = csv.writer(file)
            #     writer.writerow(Heroes)   

            Heroes= [
                # ["Ім'я героя", "Суперздібеість", "Побічні ефекти"],
                # ["One punch man","Вигравати будь-який бій одним ударом","Облисіння. Суперсила не діє на комарів"],
                # ["Род","Бог","Бог але тільки в себе в голові "],
                # ["Mello","Здатність літати","Тільки на 10 см від землі"]
            ]

            for i in range(1000):
                person = list()
                person.append(input("Ім'я вашого супер героя: "))
                person.append(input("Його суперздібність: "))
                person.append(input("Бобічні ефекти: "))
                # добавление вложенного списка
                Heroes.append(person)
                #Heroes[i-1]= person
                BreakQuestion=input("Продовжити? y/n ")
                if BreakQuestion=="No" or BreakQuestion=="n" or BreakQuestion=="no" or BreakQuestion=="NO":
                    break

            with open(TaskFile, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(Heroes)
        
        with open(TaskFile, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0], " | ", row[1], " | ", row[2])     

    if(DisChoise==3):

        TaskFile = "user.dat"

        print("Заповніть анкету для входу в клуб")
        name = input("Ваше ім'я :")
        age = int(input("Ваш вік : "))

        print("Ви передаєте анкету...")

        with open(TaskFile, "wb") as file:
            pickle.dump(name, file)
            pickle.dump(age, file)
        
        if(age>21):
            with open(TaskFile, "rb") as file:
                name = pickle.load(file)
                age = pickle.load(file)
                print("Гаразд, ваше ім'я :", name, "\tВаш вік: ", age)         
                print("Тримайте будь ласка вашу"+Fore.GREEN+"перепустку для входу")

#ColsPrint=print(*messages,sep="\n")

# try:
#     10 / 0
# except Exception as e:
#     logging.exception(e)

# logger = logging.getLogger(__name__)
# handler = logging.FileHandler('test.log', encoding='utf-8')
# formatter = logging.Formatter('%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]')
# handler.setFormatter(formatter)
# logger.addHandler(handler)

# logger.info('Давай протестируем файл на данные?')




