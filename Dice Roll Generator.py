import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("Welcome to the Dice Roll Generator!")
    
    while True:
        roll = roll_dice()
        print(f"You rolled a {roll}.")

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
