from random import choice

ROCK = 'r'
PAPER ='p'
SCISSOR ='s'
emojis = {ROCK:'🪨', PAPER:'📃', SCISSOR:'✂️'}
choiceList = tuple(emojis.keys())

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
    elif ((user_choice == ROCK and computer_choice == PAPER or
          user_choice == PAPER and computer_choice == SCISSOR or
          user_choice == SCISSOR and computer_choice == ROCK)):
        print("You lose")
    elif ((user_choice == ROCK and computer_choice == SCISSOR or
          user_choice == PAPER and computer_choice == ROCK or
          user_choice == SCISSOR and computer_choice == PAPER)):
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