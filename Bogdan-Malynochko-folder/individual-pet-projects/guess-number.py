import random;

def guessNumber():
    random_number = random.randint(1, 10);
    guessed_number = 0;
    while guessed_number != random_number:
        guessed_number = int(input("Guess the number: "));
        if guessed_number == random_number:
            print(f'Congratulations, you could guess the number! It was: {guessed_number}');
        else:
            print("You couldn't guess the number");

guessNumber();