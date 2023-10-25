from colorama import Fore,Back,Style
from colorama import init
init(autoreset=True)

print(Fore.BLUE+'\nОдного літнього дня я вирішив взяти коротку прогулянку в парку поблизу мого будинку. Сонце було яскраве, і повітря наповнювалося спокоєм. Я подавався глибше в лісову частину парку, де було тихо і спокійно.\n\nПід час моєї прогулянки я помітив чоловіка, який сидів на лавці поруч з доріжкою. Його зовнішність вразила мене: він був вельми блідий і видався дуже хворим. Його очі були поглянуті в нікуди,  губи тремтіли. Він майже не міг говорити, і я помітив, що він намагалася щось сказати, але слова виходили дуже важко.\n\nЯ підійшов до нього і запитав, чи все в порядку. Він почав примовляти кілька слів, але було важко розібрати, що він намагався сказати. Видно було, що дуже хвилювався і відчував дискомфорт. Я намагався розуміти, що він говорив, але це було вельми складно.\n\n-Скажи хоч як тебе звати друже')


def GetFirstLetter(String):
    Words = String.split()  # Розділити рядок на слова, використовуючи пробіли
    FirstLetter = ""

    for w in Words:
        FirstLetter += w[0]  # Додати першу букву кожного слова до результуючого рядка

    return FirstLetter

YourName=input()
FirstLetter = GetFirstLetter(YourName)
for c in FirstLetter:
    print("-"+c+"@*%;!")
    
# print("Перші букви кожного слова: " + FirstLetter)


print(Fore.BLUE+"-... Можливо спробуємо порахувати до трьох ? Я почну\n-Один...")
# Youcounting=""
CounterTry=0
while(CounterTry<10):
    Youcounting=input()
    if (Youcounting=="два" or Youcounting=="Два" or Youcounting=="ДВА" or Youcounting=="дВА" or Youcounting=="двА"or Youcounting=="ДВа"):
        print(Fore.BLUE+"-Непогано давай далі")
        break
    elif Youcounting=="2" or Youcounting=="3" or Youcounting=="4" or Youcounting=="5" or Youcounting=="6"or Youcounting=="7":
        print(Fore.BLUE+"-Чувак так схема не працює")
    CounterTry+=1

if(CounterTry>=8):
    print(Fore.BLUE+"-Гаразд , досить... Краще відведем тебе до лікаря ")
else:
    while(CounterTry<20):
        Youcounting=input()
        if (Youcounting=="три" or Youcounting=="Три" or Youcounting=="ТРИ" or Youcounting=="тРИ" or Youcounting=="трИ"or Youcounting=="ТРи"):
            print(Fore.BLUE+"-Молодець! Tепер гайда скоріше до лікаря")
            break
        elif Youcounting=="2" or Youcounting=="3" or Youcounting=="4" or Youcounting=="5" or Youcounting=="6"or Youcounting=="7":
            print(Fore.BLUE+"-Чувак так схема не працює")
        CounterTry+=1
if CounterTry>=15:
    print(Fore.BLUE+"-Гаразд , досить... Краще відведем тебе до лікаря ")

