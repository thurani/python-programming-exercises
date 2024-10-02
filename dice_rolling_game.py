import random

while True:
    choice = input('Do you want to roll the dice? (Y/N): ').lower()
    if choice == 'y':
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print(f'({roll1}, {roll2})')
    elif choice == 'n':
        print('Thank you for playing')
        break
    else:
        print('Invalid Choice')