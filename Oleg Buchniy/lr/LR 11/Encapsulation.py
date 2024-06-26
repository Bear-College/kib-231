import random   

from colorama import Fore,Back,Style
from colorama import init
init(autoreset=True)

class Animal:
    def __init__(self):
        self.__AnimalMakeNoise="none"
    def Get_Animal_Noise(self):
        return self.__AnimalMakeNoise
class Lizard(Animal):
    def __init__(self):
        self.__AnimalMakeNoise="Shhhh"
    def Get_Animal_Noise(self):
        return self.__AnimalMakeNoise
class Tiger(Animal):
    def __init__(self):
        self.__AnimalMakeNoise="Hrrrr"
    def Get_Animal_NoiseT(self):
        return self.__AnimalMakeNoise
class Lion(Animal):
    def __init__(self):
        self.__AnimalMakeNoise="Aaarght"
    def Get_Animal_Noise(self):
        return self.__AnimalMakeNoise
class Gorila(Animal):
    def __init__(self):
        self.__AnimalMakeNoise="UaoaAa"
    def Get_Animal_Noise(self):
        return self.__AnimalMakeNoise


class Person:
    def __init__(self):

        self.__Name = None
    def Set_Info_Human(self,NamePerson):
        self.__Name=NamePerson
    def Get_Info_Human(self):
        return self.__Name

class Gladiator(Person):
    def __init__(self):     
        self.__Health=None
        self.__Damage=None
        

    def Set_Info_Gladiators(self,Damamge,Health,NameGladiator):
        #super().Set_Info_Human(NameGladiator)
        self.__Name=NameGladiator
        self.__Health=Health
        self.__Damage=Damamge
        
    def Get_Info_Gladiators(self):
        #self.__InfoGladiators=f"Name: {super().Get_Info_Human()} Yого здоров'я:{self.__Health}, його дамаг:{self.__Damage}"
        self.__InfoGladiators=f"Name: {self.__Name} Yого здоров'я:{self.__Health}, його дамаг:{self.__Damage} "
        return self.__InfoGladiators

class ReptileGladiators(Gladiator,Lizard):
    def __init__(self):
        super().__init__()
        Lizard.__init__(self)
        self.__Ability="Здібність вкрасти зброю"
        self.__SambyakaneTotoWaSsikayNoYouZhio="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⢀⣴⠟⠉⠀⠀⠀⠈⠻⣦⡀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣀⢀⣾⠿⠻⢶⣄⠀⠀⣠⣶⡿⠶⣄⣠⣾⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⢻⣿⣿⡿⣿⠿⣿⡿⢼⣿⣿⡿⣿⣎⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡟⠉⠛⢛⣛⡉⠀⠀⠙⠛⠻⠛⠑⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣧⣤⣴⠿⠿⣷⣤⡤⠴⠖⠳⣄⣀⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣟⠻⢦⣀⡀⠀⠀⠀⠀⣀⡈⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠉⡇⠀⠀⠛⠛⠛⠋⠉⠉⠀⠀⠀⠹⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠀⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠈⠑⠪⠷⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣦⣼⠛⢦⣤⣄⡀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠲⠖⠛⠻⣿⡿⠛⠉⠉⠻⠷⣦⣽⠿⠿⠒⠚⠋⠉⠁⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⠛⠁⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀
⠀⠀⠀⠀⣰⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀
⠀⠀⠀⣰⣿⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣧⣄⠀⠀⠀⠀⠀⠀⢳⡀⠀
⠀⠀⠀⣿⡾⢿⣀⢀⣀⣦⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣫⣿⡿⠟⠻⠶⠀⠀⠀⠀⠀⢳⠀
⠀⠀⢀⣿⣧⡾⣿⣿⣿⣿⣿⡷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢿⣿⣧⠀⡀⠀⢀⣀⣀⢒⣤⣶⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
⠀⠀⡾⠁⠙⣿⡈⠉⠙⣿⣿⣷⣬⡛⢿⣶⣶⣴⣶⣶⣶⣤⣤⠤⠾⣿⣿⣿⡿⠿⣿⠿⢿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
⠀⣸⠃⠀⠀⢸⠃⠀⠀⢸⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⠟⡉⠀⠀⠀⠈⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
⠀⣿⠀⠀⢀⡏⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠀⠉⠠⠿⠟⠻⠟⠋⠉⢿⣿⣦⡀⢰⡀⠀⠀⠀⠀⠀⠀⠁
⢀⣿⡆⢀⡾⠀⠀⠀⠀⣾⠏⢿⣿⣿⣿⣯⣙⢷⡄⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣻⢿⣷⣀⣷⣄⠀⠀⠀⠀⢸⠀
⢸⠃⠠⣼⠃⠀⠀⣠⣾⡟⠀⠈⢿⣿⡿⠿⣿⣿⡿⠿⠿⠿⠷⣄⠈⠿⠛⠻⠶⢶⣄⣀⣀⡠⠈⢛⡿⠃⠈⢿⣿⣿⡿⠀⠀⠀⠀⠀⡀
⠟⠀⠀⢻⣶⣶⣾⣿⡟⠁⠀⠀⢸⣿⢅⠀⠈⣿⡇⠀⠀⠀⠀⠀⣷⠂⠀⠀⠀⠀⠐⠋⠉⠉⠀⢸⠁⠀⠀⠀⢻⣿⠛⠀⠀⠀⠀⢀⠇
⠀⠀⠀⠀⠹⣿⣿⠋⠀⠀⠀⠀⢸⣧⠀⠰⡀⢸⣷⣤⣤⡄⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⢼⡇
⠀⠀⠀⠀⠀⠙⢻⠄⠀⠀⠀⠀⣿⠉⠀⠀⠈⠓⢯⡉⠉⠉⢱⣶⠏⠙⠛⠚⠁⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠻⠄⠀⠀⠀⢀⣿⠀⢠⡄⠀⠀⠀⣁⠁⡀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⢀⣐⡟⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢠⡇
"""
    def __str__(self):
        return Fore.GREEN+f"\n {self.Get_Animal_Noise()} {self.__SambyakaneTotoWaSsikayNoYouZhio} \n{self.Get_Info_Gladiators()}, його особливість: {self.__Ability}"
    
class TigerGladiator(Gladiator,Tiger):
    def __init__(self):
        super().__init__()
        Tiger.__init__(self)
        self.__Ability="Кровотеча при ударі"
        self.__SambyakaneTotoWaSsikayNoYouZhio="""
  ⢠⡶⠛⠛⠢⣄⠀⠀⣀⣀⣀⣤⣀⣀⣀⢀⡤⠖⠛⠓⣆⠀⠀⠀
⠀⠀⣾⠁⢠⡆⠀⣌⠿⠿⠛⣻⣿⣯⠙⣛⠻⠏⠀⣠⣤⡀⢸⠀⠀⠀
⠀⠀⢹⣤⣻⠏⠚⢉⣠⣾⡵⠭⢻⠂⠠⣭⣓⠦⣀⠙⢻⣷⠟⠀⠀⠀
⠀⠀⠈⢯⠤⡤⢞⡧⠈⡵⠃⡞⢻⡈⠳⡙⢦⡘⢧⡓⢄⢾⠀⠀⠀⠀
⠀⠀⢰⠃⡾⢡⡏⡧⢾⢄⠸⠡⠛⠋⠒⠛⡠⣽⢆⢳⡘⡎⢢⠀⠀⠀
⠀⢠⡇⢸⡇⣿⢰⢻⣶⣾⡷⡄⠀⠀⠀⣾⣟⣿⡹⠋⡇⣧⠀⢇⠀⠀
⠀⢸⠀⢸⡇⢻⡸⢦⣙⡊⣿⠁⠀⠀⠀⢻⡉⠉⠀⠀⡇⣿⠀⢸⣷⣄
⠀⡾⠀⢸⣧⠘⡟⠂⠲⣤⡿⠀⠀⠀⠀⠈⠓⣜⣶⢶⠁⣿⠁⢸⣿⡏
⢀⣿⡀⠈⢻⣄⢸⡌⢷⡎⠀⠀⠀⠀⠀⠀⠆⠈⣯⣄⣤⡿⠀⢸⠁⢀
⠈⠘⣷⡀⠀⢿⣷⣿⣟⣻⡤⡷⣶⡒⡶⠞⣠⣾⣿⡶⠿⠋⢐⠆⠀⣼
⠀⠀⠹⣿⡇⠀⡎⡏⡿⣯⢽⡟⠈⣻⡁⠠⢿⣿⠟⠁⢀⢀⡾⠀⢰⡟
⠀⠀⠀⣿⣧⣀⢀⣿⢠⠈⡻⠓⠉⠉⠉⠒⢾⠙⡄⢱⣤⡿⠄⣠⡿⠃
⠀⠀⢀⡸⡛⠿⣧⣉⡋⠛⠧⢄⣀⣀⡀⣠⠾⢯⠴⠿⠏⣠⣾⣿⠃⠀
⠀⠀⠈⢳⡕⣄⠀⠙⠻⢶⣤⡀⠉⠙⠻⡁⠀⠀⠀⢀⡼⣻⣿⠃⠀⠀
⠀⠀⠀⠀⠙⣮⠑⠦⣀⠀⠉⠻⢶⣄⠀⠈⠦⡀⠖⠉⢰⣿⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠳⣤⣀⠉⠓⠄⠀⠙⢿⣤⡀⠀⠀⣠⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⣶⣤⡀⠀⠈⠻⡛⠂⠀⣉⠀⠀⠀⠀⠀⠀
"""

    def __str__(self):
        return Fore.RED+f"\n{self.Get_Animal_NoiseT()} {self.__SambyakaneTotoWaSsikayNoYouZhio} \n{super().Get_Info_Gladiators()}, його особливість {self.__Ability}"

class LionGladiator(Gladiator,Lion):
    def __init__(self):
        super().__init__()
        Lion.__init__(self)
        self.__Ability="Потужний удар"
        self.__SambyakaneTotoWaSsikayNoYouZhio="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⢀⣠⠴⢞⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣲⣿⡄⢀⡴⠋⣠⣾⣿⣿⣿⣿⣄⣀⣀⡀⠀⠀⠀⠀⠈⠓⠲⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⣼⣿⣿⣿⡟⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣶⣦⣄⡀⠀⠀⠙⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠊⠉⠀⠀⠈⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⡉⠛⢿⣷⣄⠀⠀⠈⢷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⡀⠤⠐⠒⡁⢴⣤⣤⡀⠀⠀⠀⣠⣼⣿⣿⣏⣀⣀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣷⣄⠀⠀⠹⡄⠀⠀⠀⠀⠀
⢰⣦⣍⣁⠀⠀⠀⠀⠀⠀⢾⡉⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⢸⣿⣿⣿⣿⣿⣿⣷⡄⢻⣿⣆⠀⠀⠑⠀⠀⠀⠀⠀
⠈⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠁⠁⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⡿⠋⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢻⣿⡄⠀⠀⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡻⢿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⣿⣷⠀⠀⠀⠀⠀⠀⠀
⢀⠀⠀⠀⠀⠀⠀⠀⢸⠾⠀⢀⣠⣶⠀⣠⣾⣿⣿⣿⣿⣦⡉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣇⠀⠀⠀⠀⠀⠀
⠀⢹⠁⠰⠉⠉⠒⢄⣸⡷⠿⠛⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⢇⡇⠀⠀⠀⠘⠁⣿⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠈⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀
⠀⠀⠀⠁⠀⠀⠀⠀⠀⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣯⠻⢿⣿⣿⣿⣷⣶⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢀⣿⣿⣿⣷⣶⣶⣾⣿⡿⠟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣼⣿⣿⣿⣿⣿⡍⠁⠀⠀⠀⠀
⠀⠀⢀⠞⡄⠀⠀⢠⣿⣣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠏⣼⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⢸⣀⣇⠠⠔⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⣾⣿⣿⣿⡿⢣⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠰⡀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⠟⢁⣾⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠑⡄⢸⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠚⠉⠉⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢛⣉⣤⣶⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠟⡇⠈⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠹⣿⣿⣿⣿⣿⡏⠀⣿⡀⢻⣿⣿⣿⣿⣿⣿⠟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⡀⠈⠻⣿⣿⣿⡇⠀⠸⣷⡀⢿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠈⠙⠿⣿⡄⠀⠘⢿⣦⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⡀⠀⠀⠀⠀⠀⠀⠈⠛⠿⢿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠳⠦⠄⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    def __str__(self):
        return Fore.YELLOW+f"\n{self.Get_Animal_Noise()} {self.__SambyakaneTotoWaSsikayNoYouZhio} \n{super().Get_Info_Gladiators()}, його особливість {self.__Ability}"

class GorilaGladiator(Gladiator,Gorila):
    def __init__(self):
        super().__init__()
        Gorila.__init__(self)
        self.__Ability="Оглушливий удар"
        self.__SambyakaneTotoWaSsikayNoYouZhio="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣤⠤⠽⢏⢩⣕⡚⠯⣝⡒⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⠼⣎⣿⣿⣷⣿⣿⣷⣿⣿⣷⣌⡓⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡔⣩⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢣⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡇⠀⠀⠀⠀
⠀⠀⠀⢀⠞⣨⣭⣭⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣭⣍⡻⡄⠀⠀⠀
⠀⠀⠀⡼⢸⣿⡿⠿⢿⠿⠻⠿⢿⣿⣿⣿⢿⠟⠻⡿⠿⢿⣿⣧⢱⠀⠀⠀
⢀⡖⠒⢧⢸⡏⠀⠠⣀⡀⠀⠠⡐⡈⠁⠄⠀⠀⡀⣄⡄⠀⠹⡿⢸⠐⠢⡀
⠸⡈⡩⢾⡘⣷⡄⠘⢿⣿⣦⣤⣼⣿⣿⣯⣠⣴⣿⣽⠇⢀⣼⡇⡧⠮⠁⡇
⠀⢳⡠⢊⣼⡏⠈⠀⠀⠀⣀⠪⣝⠛⠛⣻⠵⣄⠀⠀⠂⠀⢹⣧⣑⢤⡼⠁
⠀⡸⣡⣾⡿⣿⣶⣦⣄⡀⠈⠒⠉⠣⠜⠉⠙⠉⢰⣠⣴⣿⡿⡟⢿⣮⢫⡀
⣼⢕⣿⡏⠀⠈⢞⣿⡿⠂⠀⠀⠀⠐⠣⠀⠀⠀⠈⢿⣿⡍⠈⠀⢸⣿⡇⣷
⠸⣸⣿⣏⣆⠀⣾⡿⢰⣇⣨⣀⣦⠤⠧⠜⠓⠂⠤⣙⢿⣿⢀⢠⣿⣿⡇⡇
⠀⢣⣿⣿⣿⣼⣿⡇⠐⠋⡉⠀⢤⣴⡶⠶⠖⠀⠀⠤⣽⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠙⠙⢿⣿⣿⣿⣶⣮⠀⠀⠀⣠⣄⠀⠀⠀⣠⣼⣿⣿⣿⡿⠋⠝⠁⠀
⠀⠀⠀⠀⠀⠙⠏⠻⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⠟⠹⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠉⠛⠿⠛⠛⠻⠛⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" 
    def __str__(self):
        return Fore.MAGENTA+f"\n{self.Get_Animal_Noise()} {self.__SambyakaneTotoWaSsikayNoYouZhio} \n{super().Get_Info_Gladiators()}, його особливість {self.__Ability}"

class MeGladiator(Gladiator):
    def __init__(self):
        super().__init__()
        self.__Name="Oleg"
        self.__Damage="Ꝏ "
        self.__Health="Ꝏ "
        self.__Ability="One punch"
        self.__SambyakaneTotoWaSsikayNoYouZhio1="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣤⡇⡾⣿⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⡧⣿⡌⠣⣽⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⣿⡇⠀⢸⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣷⡄⢾⠙⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣡⡏⢸⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣗⡰⠋⠀⢸⡟⠀⡌⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⢷⡟⡃⠐⠀⠀⣿⣾⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⣰⡾⠛⢁⠞⠀⡇⠀⠀⠀⢸⣿⣷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠘⣧⡀⠀⠀⠈⢣⠀⠀⠀⠀⠀⣠⣾⠟⢀⡴⠋⠀⠉⠁⠀⡀⠀⠈⣿⣿⣿⣖⣒⡒⠒⠒⠲
⠠⡀⠀⠹⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠑⣄⣀⣠⣾⣿⠷⠚⠉⠀⠀⠀⠀⠀⠀⢣⠀⠀⢹⣿⣿⣏⠳⣶⣬⣥⣄
⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣤⢌⣿⣯⡍⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣸⣿⣿⣿⣷⡝⢿⣿⣯
⠀⠀⠀⠉⠫⡙⠿⢿⣛⢿⠻⠟⢉⣩⣽⣿⡟⠉⠀⠙⣏⠉⠓⢤⡀⣀⡠⠀⠀⠀⠀⠀ ⠀ ⣿⣿⣿⠻⢿⣿⣦⠹⣿
⠀⠀⠀⠀⠀⠈⠳⢄⠀⠉⠙⠉⠉⠉⠉⠉⠀⠀⠀⠀⠘⡖⠒⠒⠀⠈⠁⠀⠀⠀⠀⠀⠀ ⢰⣿⣿⣿⣷⣸⣿⣿⣷⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡖⢂⣴⣦⡄⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠀⠢⡀⠀⠀⠀⠀⢀⣀⣽⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⣈⠢⣄⠀⠀⠀⠀⠀⠀⣉⠤⠶⠾⡟⠁⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡺⠥⣀⠀⠀⠐⠋⠀⠀⣴⣎⣀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⡼⣽⣶⣤⣄⣀⡀⠀⠀⠈⢿⣿⣤⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠆⠀⡇⣿⣿⣿⣿⣧⡈⠉⢲⡒⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠉⡄⠀⠹⣿⣿⣿⣿⣿⣷⠑⣄⠙⢦⡉⠛⠻⠿⠿⠿⠛⠋⠛⠛⢿⣿⡿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⢠⣿⡀⠀⠘⠛⢿⣿⣿⡏⠀⠈⣆⠀⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⢸⣿⣷⡀⠀⠠⡄⠛⣿⣄⠀⠀⠸⠂⢀⡀⠈⢑⣶⠶⠒⢲⣚⠿⠗⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢣⠀⠀⠈⣿⣿⣧⠀⠀⠙⣦⠀⠻⣷⢤⣀⣀⣀⣿⣊⡡⠤⠒⠊⠉⠀⠀⠀⠀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠚⡇⢸⡆⠀⠀⢻⣿⣿⣧⠀⠀⢸⣧⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠶⠀⠀⠀⠀⠀⠀⠒
⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⡇⢸⡧⠀⠀⠀⢻⣿⣿⣆⠀⢸⢻⡄⠀⠘⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
        self.__SambyakaneTotoWaSsikayNoYouZhio2="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⢸⡆⢰⠀⡆⠀⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠈⡆⣧⢀⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣿⢿⣿⠟⣢⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⡆⢁⠻⢿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣴⠟⣹⣧⠏⠑⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⢸⣰⣾⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠋⢰⣿⡿⢀⠤⠁⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠀⠀⠸⢛⡿⠃⣹⣿⢻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡞⣿⢧⣼⣟⡂⠀⠀⢀⠜⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⢀⣾⡇⢠⣿⣿⣿⣏⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠃⠈⠈⢟⣧⠀⣀⢴⣢⢴⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⢸⣿⣧⣿⣿⣿⣿⣿⣧⣹⣿⡳⢄⠀⠀⠀⠀⠀
⠀⢀⠀⠀⠀⠀⠀⡘⣻⡆⠀⠹⠟⠛⢿⣇⣠⣤⠀⠈⠑⠢⢄⡀⡀⠀⠀⠀⠘⣤⣾⠉⣿⡯⣼⣿⣿⣿⣿⣿⣾⣿⣦⡱⢄⠀⠀⠀
⠈⠁⠈⣗⣄⠀⡀⢹⣿⣯⠇⠀⠀⠀⠀⣿⣿⣟⠀⠀⠀⠀⠀⠈⠙⠷⣄⡀⠀⠋⣠⣼⣟⣠⣿⣿⡟⠛⠛⠿⢿⣿⣬⣿⣦⣈⣲⠀
⠀⣿⣦⣌⠈⠛⠃⠀⢽⢷⠀⠀⠰⣿⡀⠉⠿⠋⠓⠀⠚⠉⠛⠳⠛⠀⠀⠉⠀⣤⣿⣿⣴⣿⣿⣿⠃⠀⠀⠀⠀⠀⢙⣷⣟⣿⣿⡇
⠀⣿⣿⣿⣷⣄⠀⠀⢰⣶⣃⣀⣀⣋⣙⣂⣀⣀⣀⣀⣀⣀⣀⣀⢠⣴⣂⣠⣾⣿⣿⣿⣿⠿⣿⣿⡆⠀⠀⠀⠀⠀⢸⣿⡿⣿⣿⡇
⠀⠻⣿⣿⣿⣿⣧⠀⠈⢿⡂⠀⠠⠽⣿⡿⠿⠛⠻⠋⠛⠛⠿⣿⣿⣿⣿⡿⢏⠈⠹⣿⠉⢳⣾⣿⡇⠀⠀⠀⠀⠀⠈⢻⣿⠿⠋⠀
⠀⠢⡈⠻⣿⣟⣿⣦⡀⠈⠙⠳⣄⠀⠉⠛⠦⣄⣀⣀⠀⣀⠤⠞⣩⠟⠋⠀⠀⠀⠀⠙⣆⠀⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢨⣷⣬⡙⠳⣿⣷⡀⠀⠀⠉⠻⠀⠀⠀⠘⠳⠀⠠⡤⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⢹⣇⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣼⣿⣿⣿⣷⣦⣀⣩⣦⡄⢤⣶⣿⣦⡀⠰⠒⠀⠀⠀⠀⣠⠄⠀⠀⠀⠀⢀⣤⣶⣾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⢯⡻⣿⣿⣿⣽⠛⣦⡈⠿⢤⣿⣖⡀⠀⠀⠰⠛⠁⠀⠀⠀⠀⠀⣩⣿⡟⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⡯⠏⠀⠈⢻⣿⠹⣿⡄⠈⠿⣦⡠⡙⠻⠷⢤⣤⣤⣾⣀⣠⣤⡔⣚⡩⢴⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⢻⠀⠀⠀⠀⠀⢻⣆⠈⢿⣔⠢⠘⣿⡷⣤⣀⡈⠉⠻⡇⠀⠀⠀⠠⠤⢶⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢰⡷⠀⠀⠀⠀⠀⠀⠹⣶⣼⣿⣷⣄⣘⢿⡄⠈⠙⠷⣦⣄⣄⠀⠀⢀⠀⢀⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣏⣿⡄⠀⣀⣻⣿⢿⡓⠶⠤⢾⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡇⠀⠀⠀⠀⠀⢀⣤⣾⡿⠟⠿⠿⢿⣿⣿⣷⣤⣿⣿⠟⠄⠀⠀⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠾⠿⠋⠁⠀⠀⠀⠀⠀⠀⠉⠹⠿⠿⠷⠾⠷⠶⠾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
        self.__SambyakaneTotoWaSsikayNoYouZhio3="""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠋⠉⠉⠛⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠏⠂⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣀⣤⠤⠤⠤⠆⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣷⠀⣀⡤⠴⠒⣆⠀⠀⠀⢉⣡⣤⠤⢤⡄⠀⢸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⡆⣥⠤⣴⡖⢻⣧⡀⠀⠸⣌⣻⣇⣤⠇⠀⠸⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠀⠘⠲⠾⠗⠋⠈⣳⠄⠀⠀⠀⠀⠀⠀⠀⠀⢸⣅⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⢾⡆⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢯⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⢰⣇⠀⠀⠀⠀⠀⠀⢾⠶⠀⠀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢯⣿⡀⠀⠀⠀⠀⠀⢀⣤⣧⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢏⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠀⠀⣀⡴⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⢷⠲⢶⣖⣺⣿⠏⠀⢻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⢿⣿⡿⢾⣋⣿⠿⠿⠋⠀⠀⢘⣮⠻⣍⠒⠒⠒⠦⢤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⣺⣿⡟⢁⣸⠋⠳⠦⣌⣉⣀⣀⣀⠤⠴⣿⣿⣆⠘⢿⣦⣦⣤⡆⣨⢏⣹⡶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣯⣿⣿⣟⡟⢸⡿⢷⣞⠆⠀⠀⠀⢹⣿⣿⡄⠀⠀⠈⣿⣆⢿⣿⣿⡶⠟⢁⡾⠟⠁⠈⢣⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⣄⡘⣿⠿⡟⢀⡼⠅⠐⠈⠙⠶⢤⠀⣸⢋⡉⢧⢠⡴⠛⠁⠉⠓⠶⠶⠖⠛⠁⠀⠀⠀⠀⠀⢳⡀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣿⣷⠹⠛⠾⠶⠶⠖⠉⠀⠀⠀⠀⠀⠀⠸⡆⠛⢻⣿⠋⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀
⠀⠀⠀⠀⠀⣼⣏⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⠀⢸⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⠀⠀⠀⢿⠀⠀
⠀⠀⠀⠀⣾⣿⠉⠠⠀⠀⠀⠀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢀⣸⣿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠸⡆⠀
⠀⠀⠀⣾⣻⡿⡀⠀⡀⠀⠀⣇⣿⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⠚⠧⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡯⠀⠀⠀⠀⠀⣇⠀
⠀⠀⣼⣻⣿⡇⣀⣼⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠶⠒⠒⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⢹⠀
⠀⣸⠻⣷⣿⠅⠵⠇⠀⠀⠀⢰⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⢸⠀
⢀⡏⠀⢧⣿⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠈⡇
⡸⢠⡞⣾⣿⣦⠀⠀⠀⠀⠀⣼⣷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡄⠀⠀⠀⠀⠀⠀⠀⡇
⠛⠉⠁⠛⠛⠛⠀⠀⠀⠀⠀⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠂⠀⠀⠀⠀⠀⠐⠛"""

        self.__SambyakaneTotoWaSsikayNoYouZhio4="""
⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⢀⣠⣖⠖⠚⠉⠉⠉⠈⠈⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡚⡞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠈⠓⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠈⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⡍⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣫⣭⣷⠶⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀ ⠸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠏⠀⠀⠀⠀⠀⠀⠀⠀⠴⠛⠛⠉⡁⠀⠀⠙⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀ ⠀⠀ ⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡷⠷⢿⣦⣤⣈⡙⢿⣿⢆⣴⣤⡄⠀ ⠀⠀⠀ ⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣤⡀⣸⡄⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣟⣩⣤⣴⣤⣌⣿⣿⣿⣦⣹⣿⢁⣿⣿⣄⣀⡀⠀  ⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⠋⠻⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⠛⢦⣽⣿⣿⢻⣿⣿⣿⣿⠋⠁⠘⣿⣿⣿⣿⣿⣿⣿⣼⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⠁⠀⠀⠙⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠿⣿⣯⣼⣿⡿⠟⠃⠀⠀⠀⣿⣿⣿⣿⣿⡛⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣧⣴⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⠟⠃⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⠿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠙⠛⠛⠙⢻⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡇⠀⠘⠃⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡟⢿⣿⣆⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡼⠁⢀⣀⡀⠀⠀⠀⣦⣄⠀⣠⡄⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣷⣬⢻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⣰⣿⡿⠿⠦⢤⣴⣿⣿⣷⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠒⣿⣿⣿⡿⠟⠹⣼⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡖⠀⢠⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡿⣾⣿⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣆⣀⣀⣤⣴⣶⣶⣾⣿⣷⣦⣴⣼⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡇⣿⣿⡛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⡟⠛⠛⠻⠛⠛⠛⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠓⢁⣬⣿⠇⠀⠀⠀⠀⠀⢠⡀⠀⠀⠀⠀⠀⢰⡿⣻⠇⠀⠀⠀⠀⠀⣠⣶⣶⣶⣶⣿⣿⡿⣿⣿⣿⣿⢎⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢐⣯⠞⠁⠀⠀⠀⠀⠀⠀⣄⠱⣄⠀⠀⠀⠀⠸⡧⠟⠆⠀⠀⠀⠀⠘⠿⢿⠿⠿⣿⡿⣿⠃⣿⣿⣿⡟⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⡈⠂⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢠⣿⠀⣿⣿⣿⡏⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⡄⠀⠀⠑⠄⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣦⣦⣼⡏⠳⣼⢿⠟⠂⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⢠⣷⣦⣤⣀⣀⣀⣴⣿⣿⣿⣿⣿⡿⢻⢎⡻⢎⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡑⣷⡅⠀⠁⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

        self.__MySkin={
            1:self.__SambyakaneTotoWaSsikayNoYouZhio1,
            2:self.__SambyakaneTotoWaSsikayNoYouZhio2,
            3:self.__SambyakaneTotoWaSsikayNoYouZhio3,
            4:self.__SambyakaneTotoWaSsikayNoYouZhio4
        }
        self.RandomSkin=random.randint(1,4)
    def __str__(self):
        return f"\n{self.__MySkin[self.RandomSkin]} \n На душе pain,\n В голове gain,\n За окном снег,\n My name is {self.__Name}  \n\nMy damage: {self.__Damage}, my health: {self.__Health}, my особливість {self.__Ability}"

Gladiator1=ReptileGladiators()
Gladiator2=TigerGladiator()
Gladiator3=LionGladiator()
Gladiator4=GorilaGladiator()
Me=MeGladiator()

InputName=input("Іnput Name of your gladiator ")
InputDamage=int(input("Іnput Damage of gladiator  "))
InputHealth=int(input("Input Health of gladiator  "))
Gladiator1.Set_Info_Gladiators(InputDamage,InputHealth,InputName)
Gladiator2.Set_Info_Gladiators(InputDamage,InputHealth,InputName)
Gladiator3.Set_Info_Gladiators(InputDamage,InputHealth,InputName)
Gladiator4.Set_Info_Gladiators(InputDamage,InputHealth,InputName)
Gladiators={
    1:Gladiator1,
    2:Gladiator2,
    3:Gladiator3,
    4:Gladiator4,
    5:Me
}

ChoiseGladiator=int(input("\nChoise Gladiator: \n1 - ReptileGladiators \n2 - TigerGladiator \n3 - LionGladiator \n4 - GorilaGladiator \n5 - Creator Творець (AKA One punch man)\n"))
if ChoiseGladiator in [1,2,3,4,5]:
    print(Gladiators[ChoiseGladiator])
else:
    print("Не правильно введені дані")


