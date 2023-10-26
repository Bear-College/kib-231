print("Оберіть область:")
print("1. Глобальний контекст")
print("2. Локальний контекст")
print("3. Приховування змінних")
print("4. Nonlocal")
print("5. Global")

choice = input("")

if choice == '1':
    name = "Tom"
 
 
    def say_hi():
        print("Hello", name)
 
 
    def say_bye():
        print("Good bye", name)
 
    say_hi()
    say_bye()

elif choice == '2':
    def say_hi():
        name = "Sam"
        surname = "Johnson"
        print("Hello", name, surname)
 
 
    def say_bye():
        name = "Tom"
        print("Good bye", name)
    
    say_hi()
    say_bye()

elif choice == '3':
    name = "Tom"
 
 
    def say_hi():
        name = "Bob"        # Приховуєм
        print("Hello", name)
    
    
    def say_bye():
        print("Good bye", name)
    
    
    say_hi()    # Hello Bob
    say_bye()   # Good bye Tom

elif choice == '4':
    def outer():  # внешняя функция
        n = 5
 
        def inner():    # вложенная функция
            nonlocal n  # указываем, что n - это переменная из окружающей функции
            n = 25
            print(n)
 
        inner()     # 25
        print(n)
 
 
    outer()          # 25
    
elif choice == '5':
    name = "Tom"
 
 
    def say_hi():
        global  name
        name = "Bob"        # изменяем значение глобальной переменной
        print("Hello", name)
    
    
    def say_bye():
        print("Good bye", name)
    
    
    say_hi()    # Hello Bob
    say_bye()   # Good bye Bob

else:
    print("Невірний вибір операції")
