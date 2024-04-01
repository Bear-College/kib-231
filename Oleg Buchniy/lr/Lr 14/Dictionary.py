import random
from collections import Counter

Diseases= {1: "Ідеальне здоров'я ", 2: "Мігрень", 3: "Грип",4: "Аутоімунний теріоїдит", 5: "Алопеція", 6: "Депресія"}
Profecions={1: "Системний адміністратор ", 2: "Лікар ендокринолог", 3: "Маркетолог",4: "Бухгалтер", 5: "Директор нафтопереробного заводу", 6: "Найманий вбивця"}
Larges={1: "Костюм клоуна", 2: "Пістолет з патронами", 3: "Журнал бойскаута",4: "Сторожовий пес", 5: "PS5", 6: "Шахмати"}
Hobbies={1: "Регбі", 2: "Хобіхорсинг", 3: "Бракон'єрство",4: "Програмування", 5: "Риболовля", 6: "Стільба"}


players = {
    1: {
        "name": "You",
        "profecion": "Лікар ендокринолог",
        "large": "Ствол з патронами",
        "age": "20",
        "hobby": "Хобіхорсинг",
        "health": "Ідеально здоровий",
        "isManiak": False

    },
    2: {
        "name": "Bob",
        "profecion": "Маркетолог",
        "large": "Костюм клоуна",
        "age": "40",
        "hobby": "Полювання на звірів",
        "health": "Ідеально здоровий",
        "isManiak": False

    },
    3: {
        "name": "Tom",
        "profecion": "Маркетолог",
        "large": "Костюм клоуна",
        "age": "40",
        "hobby": "Полювання на звірів",
        "health": "Ідеально здоровий",
        "isManiak": False

    },
    4: {
        "name": "Tаm",
        "profecion": "Маркетолог",
        "large": "Костюм клоуна",
        "age": "40",
        "hobby": "Полювання на звірів",
        "health": "Ідеально здоровий",
        "isManiak": False

    }

}

players_opened = {
    1: {
        "profecion": "Лікар ендокринолог"
    },
    2: {
        "profecion": "Маркетолог"
    },
    3: {
        "profecion": "Маркетолог"
    },
    4: {
        "profecion": "Маркетолог"
    }

}

#ГОЛОСУВАННЯ АНОНІМНЕ
def vote_to_eliminate(amount_players): 
    print("Гравці можуть голосувати за виключення іншого гравця.")
    print("Введіть номер гравця, за якого ви голосуєте для виключення.")
    
    # Створення словника для зберігання голосів кожного гравця
    votes = Counter()

    # Голосування кожного гравця
    for i, player in enumerate(amount_players, 1):
        vote = random.choice(amount_players)
        votes[vote] += 1
        print(f"{i}-й Гравець  проголосував за: {vote}-ого ")

    vote = int(input(f"Ваше слово (напишіть номер гравця якого бажаєте вилучити): "))
    if vote in amount_players:
        pass
    else:
        print("Голосуєш в себе ")
        vote=1
    votes[vote] += 1


    # Знаходження гравця з найбільшою кількістю голосів
    eliminate_player = votes.most_common(1)[0][0]

    if(eliminate_player==1):
        print("Поздравляю тебе вигнали")
    else:
        print(f"Гравець {eliminate_player} був вилучений із гри за голосами {votes[eliminate_player]} учасників.")

    # Повертаємо номер вилученого гравця
    return eliminate_player


# Цикл видачі всім характеристик
for i in players:
    ProfecionChoise=random.randint(1,6)
    players[i]["profecion"]=Profecions[ProfecionChoise]

    LargeChoise=random.randint(1,6)
    players[i]["large"]=Larges[LargeChoise]

    AgeChoise=random.randint(19,80)
    players[i]["age"]=AgeChoise

    HobbyChoise=random.randint(1,6)
    players[i]["hobby"]=Hobbies[HobbyChoise]

    HealthChoise=random.randint(1,6)
    players[i]["health"]=Diseases[HealthChoise]

    if HealthChoise!=1:
        StageDiseases=random.randint(-25,100)
        if StageDiseases<=0:
            StageDiseases="Індкубаційний період"
        players[i]["health"]+=f", Cтадія хвороби {StageDiseases} %"
    


KeyName="name"
KeyProfecion="profecion"
for p in players:
    ProfecionToNewDictionary=f"Учасник {p} : {players[p][KeyName]} , його професія : {players[p][KeyProfecion]}"
    print(ProfecionToNewDictionary)
    players_opened[p]["profecion"]=ProfecionToNewDictionary
    del players[p]["profecion"]



# Приклад використання
#list_players = list(range(1, players_count + 1))
    
# list_players = list(players.keys())
# zyibav_player = vote_to_eliminate(list_players)
# print("Вилучений гравець:", zyibav_player)
# del players[zyibav_player]

RoundCounter=0
while RoundCounter<=2:
    for p in players:
        #if при виборі користувача ,недороблений 
        """
        if p ==1:
            print("Перший раунд закінчився. Зараз буде другий раунд в якому гравці будуть по черзі відкривати характеристики які вважають доцільними, після чого буде проведене голосування на виключення гравця який на вашу думку не проходить в бункер")
            print("\nОберіть характеристику яку бажаєте відкрити іншим учасникам")
            #цикл для виводу усіх доступних характеристик для вибору користувача
            for u in players:
        """        
        random_key = random.choice(list(players[p].keys())) 
        #random bez Maniak-a
        #random_key = random.choice([key for key in players.keys() if key != "isManiak"])

        ChitsToNewDictionary= {players[p][random_key]: f"Його\її {random_key} : {players[p][random_key]}"}   
        print(f"Учасник {p} відкрив своє {random_key} : {players[p][random_key]}")
        players_opened[p].update(ChitsToNewDictionary)
        del players[p][random_key]
    
    print("\nНастав час голосування \nХарактеристики учасників що залишилися: ")
    for k in players:
        KeyProfecion="profecion"
        print(f"Учасник {k} його\її характеристики: {players_opened[k][KeyProfecion]}")
    list_players = list(players.keys())
    zyibav_player = vote_to_eliminate(list_players)
    print("Вилучений гравець:", zyibav_player)
    del players[zyibav_player]


