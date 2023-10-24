
while True:
    print("exit - exit the program")
    word = input("enter the word: ")

    if word.lower() == "exit":
        exit()
    else:
        word = word.split()
        for x in word:
            print(x[0])
