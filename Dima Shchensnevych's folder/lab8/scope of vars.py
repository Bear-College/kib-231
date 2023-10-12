kil = 1

def first_par():
    kil = 2
    print("Кількість присутніх студентів на першій парі: ", kil)

def second_par():
    global kil
    kil = 5
    print("Кількість присутніх студентів на другій парі: ", kil)

def third_par(): 
    print("Кількість присутніх студентів на третій парі: ", kil)

def fourth_par():
    kil = 6
    def fifth_par():
        nonlocal kil
        kil = 7
        print("Кількість присутніх студентів на п'ятій парі: ", kil)
    fifth_par()
    print("Кількість присутніх студентів на четвертій парі: ", kil)
    
first_par()
second_par()
third_par()
fourth_par()


