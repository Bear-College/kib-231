players = {
    1: {
        "name": "Yought",
        "profecion": "Лікар ендокринолог",
        "large": "Ствол з патронами",
        "age": "20",
        "hobby": "Хобіхорсинг",
        "health": "Ідеально здоровий",
        "isManiak": True

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

# for n in players:
#     for c in players[n]:
#         print(f"Учасник {n} його\її характеристики: {players[n][c]}")


# for k in players:
#    *other_characteristik,is_maniak = players[k]
#    print(f"Учасник {k} його\її характеристики: {players[k]} {other_characteristik}")

for k in players:
    print(" ")
    *other_characteristik,is_maniak = players[k]
    print(f"Учасник {k} його\її характеристики:  ")
    for m in players[k]:
        if m == "isManiak":
            pass
        else:
            print(f"{m} : {players[k][m]} ")
        
    # if players[k].values == "isManiak":
    #     pass
    # else:
    #     print(f"Учасник {k} його\її характеристики: {players[k]} ")

number_maniak=int(input("Вгадай хто маніак, напиши номер учасника якого ти вважаєш ман'яком "))
if players[number_maniak][is_maniak]== True:
    print("Вітаю, ти вгадав, залишився живий")
else:
    print("Вітаю, ти не вгадав, ти помер")


