from random import choice

emojis = {'r':'🪨', 'p':'📃', 's':'✂️'}
choiceList = ('r', 'p', 's')

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or Scissors? (r/p/s) : ").lower()
        if user_choice in choiceList:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_the_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif ((user_choice == "r" and computer_choice == "p" or
          user_choice == "p" and computer_choice == "s" or
          user_choice == "s" and computer_choice == "r")):
        print("You lose")
    elif ((user_choice == "r" and computer_choice == "s" or
          user_choice == "p" and computer_choice == "r" or
          user_choice == "s" and computer_choice == "p")):
        print("You Win")

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = choice(choiceList)

        display_choices(user_choice, computer_choice)

        determine_the_winner(user_choice, computer_choice)

        play_again = input("Continue? (y/n) : ").lower()
        if play_again == "n":
            print("Thanks for playing!")
            break

play_game()