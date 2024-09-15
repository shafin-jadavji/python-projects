'''
Write a program to simulate a game of Rock, Paper, Scissors.  
The game will prompt the player to choose rock, paper, or scissors by typing 'r', 'p', or 's'. 
The computer will randomly select its choice. The game will then display both choices 
using emojis and determine the winner based on the rules. 
'''
# loop
    # Ask user to make choice of r/p/s
    # if choice not valid
        # print Invalid Choice
        # return to loop  
    # computer to randomely pick choice
    # display emoji for player choice
    # display emoji for computer choice
    # determine winner based on rules
    # Ask to play again y/n
    # if n
        # terminate

import random

choices = ("r", "p", "s")
emojis ={ "r": "🪨", "p": "📃", "s": "✂️"}

while True:
    user_choice = input("Rock, Paper, Scissors (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue

    computer_choice = random.choice(choices)

    # display emoji for player choice
    # display emoji for computer choice
    print(f"You chose {emojis[user_choice]}")
    print (f"Computer chose {emojis[computer_choice]}")

    # determine winner based on rules
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "p" and computer_choice == "r") or
        (user_choice == "s" and computer_choice == "p")
    ):
        print("You win!")
    else:
        print("You lose!")

    continue_playing = input("Continue y/n: ").lower()
    if continue_playing == "n":
        break

