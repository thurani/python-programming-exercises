import random

randomNumber = random.randint(1, 100)

while True:
    try:
        guessedNumber = int(input("Guess a number between 1 and 100: "))
        if guessedNumber < randomNumber:
            print("Too low!")
        elif guessedNumber > randomNumber:
            print("Too high!")
        else:
            print("Congratulations! You got it right!")
            break
    except ValueError:
        print("Please enter a valid number")