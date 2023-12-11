

import random
from colorama import Fore,Back,Style
from colorama import init
init(autoreset=True)
YourChoise=input("Виконати завдання чи бути щасливим? ")

if(YourChoise=="бути щасливим" or YourChoise=="Бути щасливим" or YourChoise=="бути Щасливим" or YourChoise=="БУТИ ЩАСЛИВИМ" or YourChoise=="Щасливим" or YourChoise=="ЩАСЛИВИМ" or YourChoise=="щасливим" or YourChoise=="бути" or YourChoise=="БУТИ щасливим" or YourChoise=="Бутищасливим"or YourChoise=="be happy"or YourChoise=="Be happy"or YourChoise=="behappy"or YourChoise=="be happy "or YourChoise=="BE HAPPY"or YourChoise=="h" or YourChoise=="щ"):
    class Gladiator:
    
        def __init__(self):
            self.name = None    
            #self.age = 1        # штучно доданий атрибут
            self.Heals=None
            self.Damage=0
            self.Armor=None
            self.Teritory=None
            self.Skin=None

        # def Set_Info_Gladiators(self,SomeDamage):
        #     InfoGladiators=f"Його броня:{self.Armor}, його здоров'я:{self.Heals}, його дамаг:{SomeDamage}"
        #     InfoGladiators.center(52)
        #     return InfoGladiators
        def Set_Info_Gladiators(self):
            InfoGladiators=f"Його броня:{self.Armor}, його здоров'я:{self.Heals}, його дамаг:{self.Damage}"
            InfoGladiators.center(52)
            return InfoGladiators

    def Is_Number(value):
        try:
            float(value)  # Спробa перетворити введене значення в число з плаваючою комою
            return False
        except ValueError:
            return True

    tom = Gladiator()
    tom.name=input("Введіть ім'я гладіатора : ")
    tom.Armor=random.randint(1, 80)
    tom.Heals=1000
    tom.Damage

    Crux=[
        "У мене немає ваги, але я можу зважити світ. Я завжди росту, але ніколи не стаю вищим. Що це?",
        Fore.GREEN+"Що таке замикання",
        "Всім потрібен мене, але ніхто мене не бачить."
    ]
    AnswerCrux=[
        "Тінь",
        "Не знаю",
        "Повітря"
    ]

    RandCrux = random.randint(1, 3)
    YouGotThis=AnswerCrux[RandCrux-1]
    RandCrux=Crux[RandCrux-1]
    AnswerCorrectCheck=False
    UserSelection=""

    while Is_Number(UserSelection) :
        
        tom.Damage=str(input(f"Яка буде шкода у гладіатора {tom.name} ,але не більше 200 (для більшої шкоди потрібно відгадати загадку ,для цього напишіть слово 'загадка'): "))
        
        try:
            UserSelection=float(tom.Damage)
            if(float(tom.Damage)>200 ):
                tom.Damage=200
            elif(float(tom.Damage)<=200):
                print("Good")
            
        except :
            UserSelection=str(tom.Damage)
            
        try:
            if(UserSelection.lower() in ["загадка", "з","crux","mystery"]):
                print(RandCrux)
                YourAnswer=input("Ваша відповідь: ")
                if(YourAnswer.lower()==YouGotThis.lower()):
                    print("Вітаємо ви відгадали! Ваша шкода необмежена!")
                    try:
                        tom.Damage=float(input(Fore.BLUE+f"Яка буде шкода у гладіатора {tom.name} (тепер не обмежено) : "))
                        Fore.RESET
                        break
                    except:
                        tom.Damage=0
                        break
                        
                        
                else:
                    print("Нажаль ви не відгадали \n")
            elif(Is_Number(UserSelection)==True):
                print("\nНеправильно введені дані")
        except:
            pass
                
        """
        tom.Damage=input(f"Яка буде шкода у гладіатора {tom.name} ,але не більше 200 (для більшої шкоди потрібно відгадати загадку ,для цього напишіть слово 'загадка'): ")
        UserSelection=float(tom.Damage)
        if(tom.Damage>200 and AnswerOfCrux==False):
            tom.Damage=200
        elif(tom.Damage<=200):
            print("Good")
        elif(tom.Damage>200 and AnswerOfCrux==True):
            print("Good")
        else:
            UserSelection=str(tom.Damage)
            if(UserSelection.lower() in ["загадка", "з","crux","mystery"]):
                print(RandCrux)
                YourAnswer=input("Ваша відповідь: ")
                if(YourAnswer.lower()==YouGotThis.lower()):
                    print("Вітаємо ви відгадали! Ваша шкода необмежена!")
                    tom.Damage=float(input(Fore.BLUE+f"Яка буде шкода у гладіатора {tom.name} (тепер не обмежено) : "))
                    AnswerOfCrux=True

                else:
                    print("Нажаль ви не відгадали")
            else:
                print("Неправильно введені дані")  
                """  
    tom.Skin="-_-"
    tom.Teritory=Fore.RED+(" 00011010101011010101010                            10101010101011010101010 " 
              +f"\n 00011010101011010101                                  01010101011010101010 "
              +f"\n 00011010101011010{tom.name.center(40)}10101011010101010 "
              +f"\n 00011010101011{tom.Skin.center(45)} 01011010101010 "
              +f"\n 00011010101{tom.Set_Info_Gladiators().center(52)}11010101010 "
               +"\n 00011010                                                          10101010 ")
    
    print(tom.Teritory)
    bob = Gladiator()
    bob.name="Bob"
    bob.Heals=1000
    bob.Armor=random.randint(10,80)
    bob.Damage=random.randint(10,999)
    bob.Skin="+_="
    bob.Teritory=(" 00011010                                                          10101010 "
              +f"\n 00011010101{bob.Set_Info_Gladiators().center(52)}11010101010 "
              +f"\n 00011010101011{bob.Skin.center(46)}01011010101010 "
              +f"\n 00011010101011010{bob.name.center(40)}10101011010101010 "
               +"\n 00011010101011010101                                  01010101011010101010 "
               +"\n 00011010101011010101010                            10101010101011010101010 ")
    print(bob.Teritory)

    BattleCry=input("Введіть бойове гасло для початку битви: ")
    print(BattleCry+"!!")
    # DamageResultGladiatorTom=tom.Damage/100 *bob.Armor
    # DamageResultGladiatorBob=bob.Damage/100 *tom.Armor
    
    print(f"Результати бою: \nЗдоров'я гладіатора {tom.name}: {tom.Heals-(bob.Damage / 100 *tom.Armor):.2f}, нанесена ним шкода: {(tom.Damage / 100 *bob.Armor):.2f} \nЗдоров'я гладіатора {bob.name}: {bob.Heals-(tom.Damage / 100 *bob.Armor):.2f}, нанесена ним шкода: {(bob.Damage / 100 *tom.Armor):.2f}")

else:
    class Dog:
        def __init__(self,LifeExpectancyD ,NutriotionD,):
            self.LifeExpectancyD=LifeExpectancyD
            self.NutriotionD=NutriotionD
    class Cat:
        def __init__(self,LifeExpectancyC ,NutriotionC,):
            self.LifeExpectancyC=LifeExpectancyC
            self.NutriotionC=NutriotionC
    class Snake:
        def __init__(self,LifeExpectancyS ,NutriotionS,):
            self.LifeExpectancyS=LifeExpectancyS
            self.NutriotionS=NutriotionS
    class Fish:
        def __init__(self,LifeExpectancyF ,NutriotionF,):
            self.LifeExpectancyF=LifeExpectancyF
            self.NutriotionF=NutriotionF
    
    Husky=Dog("\nСередня тривалість життя: 12-15 років","\nЇжа в день: Від 2,5 до 4 чашок сухого корму (приблизно 400-1000 грамів), поділеного на дві порції. Кількість їжі може змінюватися в залежності від розміру та активності собаки.")
    Bulldog=Dog("\nСередня тривалість життя: 10-12 років","\nЇжа в день: Приблизно 1-1,5 чашки сухого корму (приблизно 200-350 грамів), поділеного на дві порції.")
    Rottweiler=Dog("\nСередня тривалість життя: 10-12 років.","\nЇжа в день: Від 2,5 до 3,5 чашок сухого корму (приблизно 500-900 грамів), поділеного на дві порції.")
    GermanShepherd=Dog("\nСередня тривалість життя: 9-13 років.","\nЇжа в день: Від 3 до 4 чашок сухого корму (приблизно 700-1000 грамів), поділеного на дві-три порції.")
    Doberman=Dog("\nСередня тривалість життя: 10-12 років.","\nЇжа в день: Від 2 до 3 чашок сухого корму (приблизно 400-900 грамів), поділеного на дві порції.")

    Dogs={
        1:f"Хаскі ", 
        2:  f"Бульдог ", 
        3:  f"Ротвейлер ",
        4:  f"Овчарка ",
        5:  f"Доберман "
    }

    Maikun=Cat("\nСередня тривалість життя: 10-13 років.","Їжа в день: Від 1/2 до 3/4 чашки сухого корму або консервів (приблизно 60-90 грамів), поділеного на дві порції.")
    Angora=Cat("\nСередня тривалість життя: 15-20 років.","Їжа в день: Зазвичай від 1/4 до 1/2 чашки сухого корму або консервів (приблизно 30-60 грамів), поділеного на дві порції.")
    Ragdoll=Cat("\nСередня тривалість життя: 12-17 років.","Їжа в день: Від 1/2 до 3/4 чашки сухого корму або консервів (приблизно 60-90 грамів), поділеного на дві порції.")
    Siamese=Cat("\nСередня тривалість життя: 12-15 років.","\nЇжа в день: Від 1/4 до 1/2 чашки сухого корму або консервів (приблизно 30-60 грамів), поділеного на дві порції.") 
    Persian=Cat('\nСередня тривалість життя: 12-16 років.',"\nЇжа в день: Зазвичай від 1/4 до 1/2 чашки сухого корму або консервів (приблизно 30-60 грамів), поділеного на дві порції.")

    Cats={
        1:f"Мейкун  ", 
        2:  f"Ангора", 
        3:  f"Рагдол",
        4:  f"Сиамський кіт ",
        5:  f"Персицький кіт "
    }

    PythonRegius=Snake("\nСередня тривалість життя: 20-30 років або більше.","\nЇжа в день: Ці змії зазвичай годуються кожні 7-14 днів гризунами, такими як миші або щури, в залежності від розміру і віку.")
    NerodiaSipedon=Snake("\nСередня тривалість життя: 10-15 років.","\nЇжа в день: Зазвичай харчується рибою та жабами.")
    ElapheGuttata=Snake("\nСередня тривалість життя: 15-20 років або більше.","\nЇжа в день: Зазвичай годується мишими або щурами кожні 7-14 днів, в залежності від розміру.")
    EpicratesCenchria=Snake("\nСередня тривалість життя: 15-20 років або більше.","\nЇжа в день: Харчується гризунами, такими як миші, кролики або щури, приблизно кожні 7-14 днів.")
    MoreliaViridis=Snake("\nСередня тривалість життя: 15-20 років або більше.","\nЇжа в день: Зазвичай годується гризунами, такими як миші, кролики або птахи, кожні 2-4 тижні, в залежності від розміру та віку.")

    Snakes={
        1:f"Королівська пітоновидна змія  ", 
        2:  f"Болотяна змія ", 
        3:  f"Була змія ",
        4:  f"Шлунчак  ",
        5:  f"Зелена деревна змія "
    }

    SmallFish=Fish("\nСередня тривалість життя: 2-3 роки.","\nПочті не їдять")
    NotSmallFish=Fish("\nСередня тривалість життя: 2-4 роки.","\nМало жеруть")
    NormSizeFish=Fish("\nСередня тривалість життя: 3-5 років.","\nНорм жруть")
    NotBigFish=Fish("\nСередня тривалість життя: 4-6 років або більше.","\nНормально так жруть")
    BigFish=Fish("\nСередня тривалість життя: 5-10 років або більше.","\nЖруть як не в себе")

    Fishes={
        1:f"Маленька  ", 
        2:  f"Не дуже маленька ", 
        3:  f"Нормальна ",
        4:  f"Не дуже велика ",
        5:  f"Велика "
    }

    Animals={
        1:Fore.MAGENTA+"Dogs",
        2:Fore.BLUE+"Cats",
        3:Fore.YELLOW+"Snakes",
        4:Fore.GREEN+"Fishes"
    }

    print("Оберіть тварину про яку хочете дізнатись ?")
    for i in Animals:
        print( Animals[i])
    ChouseAnimals=int(input("Введіть число від 1-4: "))
    
    if(ChouseAnimals==4):
        print(Fore.GREEN+"Oберіть породу тварини про яку хочете дізнатись інформацію")
        for Breed in Fishes:
            print(Fishes[Breed])

        ChouseBreed=int(input(Fore.GREEN+"Введіть число від 1-5: "))
        if ChouseBreed in [1,2,3,4,5]:
            
            Fishes={
                1:f"Маленька  "+Fore.RESET+f"{SmallFish.LifeExpectancyF} {SmallFish.NutriotionF} ", 
                2:  f"Не дуже маленька "+Fore.RESET+f"{NotSmallFish.LifeExpectancyF} {NotSmallFish.NutriotionF}", 
                3:  f"Нормальна "+Fore.RESET+f"{NormSizeFish.LifeExpectancyF} {NormSizeFish.NutriotionF}",
                4:  f"Не дуже велика "+Fore.RESET+f"{NotBigFish.LifeExpectancyF} {NotBigFish.NutriotionF}",
                5:  f"Велика "+Fore.RESET+f"{BigFish.LifeExpectancyF} {BigFish.NutriotionF}"
            }
            print(Fishes[ChouseBreed])
        else:
            print(Fore.GREEN+"Неправильно введені дані")

    elif(ChouseAnimals==2):
        print(Fore.BLUE+"Oберіть породу тварини про яку хочете дізнатись інформацію")
        for Breed in Cats:
            print(Cats[Breed])

        ChouseBreed=int(input(Fore.BLUE+"Введіть число від 1-5: "))
        if ChouseBreed in [1,2,3,4,5]:
            
            Cats={
            1:"Мейкун  "+Fore.RESET+f"{Maikun.LifeExpectancyC} {Maikun.NutriotionC} ", 
            2:  f"Ангора "+Fore.RESET+f"{Angora.LifeExpectancyC} {Angora.NutriotionC}", 
            3:  f"Рагдол "+Fore.RESET+f"{Ragdoll.LifeExpectancyC} {Ragdoll.NutriotionC}",
            4:  f"Сиамський кіт "+Fore.RESET+f"{Siamese.LifeExpectancyC} {Siamese.NutriotionC}",
            5:  f"Персицький кіт "+Fore.RESET+f"{Persian.LifeExpectancyC} {Persian.NutriotionC}"
                }
            
            print(Cats[ChouseBreed])
        else:
            print(Fore.BLUE+"Неправильно введені дані")

    elif(ChouseAnimals==3):
        
        print(Fore.YELLOW+"Oберіть породу тварини про яку хочете дізнатись інформацію")
        for Breed in Snakes:
            print(Snakes[Breed])

        ChouseBreed=int(input(Fore.YELLOW+"Введіть число від 1-5: "))
        if ChouseBreed in [1,2,3,4,5]:
            
            Snakes={
                1:f"Королівська пітоновидна змія  "+Fore.RESET+f"{PythonRegius.LifeExpectancyS} {PythonRegius.NutriotionS} ", 
                2:  f"Болотяна змія "+Fore.RESET+f"{NerodiaSipedon.LifeExpectancyS} {NerodiaSipedon.NutriotionS}", 
                3:  f"Була змія "+Fore.RESET+f"{ElapheGuttata.LifeExpectancyS} {ElapheGuttata.NutriotionS}",
                4:  f"Шлунчак  "+Fore.RESET+f"{EpicratesCenchria.LifeExpectancyS} {EpicratesCenchria.NutriotionS}",
                5:  f"Зелена деревна змія "+Fore.RESET+f"{MoreliaViridis.LifeExpectancyS} {MoreliaViridis.NutriotionS}"
                }
            print(Snakes[ChouseBreed])
        else:
            print(Fore.YELLOW+"Неправильно введені дані")

    elif(ChouseAnimals==1):
        
        print(Fore.MAGENTA+"Oберіть породу тварини про яку хочете дізнатись інформацію")
        for Breed in Dogs:
            print(Dogs[Breed])

        ChouseBreed=int(input(Fore.MAGENTA+"Введіть число від 1-5: "))
        if ChouseBreed in [1,2,3,4,5]:
            
            Dogs={
                1:f"Хаскі : "+Fore.RESET+f"{Husky.LifeExpectancyD} {Husky.NutriotionD} ", 
                2:  f"Бульдог "+Fore.RESET+f"{Bulldog.LifeExpectancyD} {Bulldog.NutriotionD}", 
                3:  f"Ротвейлер "+Fore.RESET+f"{Rottweiler.LifeExpectancyD} {Rottweiler.NutriotionD}",
                4:  f"Овчарка "+Fore.RESET+f"{GermanShepherd.LifeExpectancyD} {GermanShepherd.NutriotionD}",
                5:  f"Доберман "+Fore.RESET+f"{Doberman.LifeExpectancyD} {Doberman.NutriotionD}"
            }
            print(Dogs[ChouseBreed])
        else:
            print(Fore.MAGENTA+"Неправильно введені дані")
    else:
        print("Неправильно введені дані")