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

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

emojis ={ ROCK: "🪨", PAPER: "📃", SCISSORS: "✂️"}
choices = (tuple(emojis.keys()))

def get_user_choice():
    """
        Get user choice of Rock, Paper, or Scissors.
        
        This function prompts the user to enter their choice of 'r', 'p', or 's' and
        validates the input. If the user enters an invalid choice, the function will
        print an error message and prompt the user again until a valid choice is
        entered.
        
        Returns:
            str: The user's choice of 'r', 'p', or 's'.
        """

    while True:
        user_choice = input("Rock, Paper, Scissors (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    """
    Displays the user's and computer's choices in the game of Rock, Paper, Scissors using emojis.
    
    Args:
        user_choice (str): The user's choice of 'r', 'p', or 's'.
        computer_choice (str): The computer's randomly selected choice of 'r', 'p', or 's'.
    
    Returns:
        None
    """

    print(f"You chose {emojis[user_choice]}")
    print (f"Computer chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of a round of Rock, Paper, Scissors based on the user's 
    and computer's choices.
    
    Args:
        user_choice (str): The user's choice of 'r', 'p', or 's'.
        computer_choice (str): The computer's randomly selected choice of 'r', 'p', or 's'.
    
    Returns:
        None
    """

    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == PAPER and computer_choice == ROCK) or
        (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    """
    Plays a game of Rock, Paper, Scissors with the user.

    The function prompts the user to make a choice, generates a random choice for the computer, 
    displays the choices, determines the winner, and asks the user if they want to continue 
    playing. The game loop continues until the user chooses to stop playing.
    """

    while True:

        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        continue_playing = input("Continue y/n: ").lower()
        if continue_playing == "n":
            break

if __name__ == "__main__":
    play_game()
