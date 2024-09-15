'''
Write a program that simulates rolling a pair of dice. 
Each time the program runs, it should randomly generate two numbers between 1 and 6 (inclusive), 
representing the result of each die. The program should then display the results 
and ask if the user would like to roll again. 
'''
import random

num_rolls = 0

# Loop
while True:

    # ask if they want to roll the dice
    roll_again = input("Do you want to roll the dice? (y/n): ").lower()

    # if y, 
    if roll_again == "y":

        # increment num_rolls
        num_rolls += 1

        # create an empty list of dice
        # dice = []

        # ask for the number of dice to roll
        # num_dice = input("How many die would you like to roll? (2-6): ")

    #   roll the two dice (two random numbers from 1 to 6 inclusive)
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

    #   display the results
        print(f"({die1}, {die2})")

    # if n,
    elif roll_again == "n":
        
    #   print thank you for playing and the number of rolls
        print(f"Thank you for playing! Dice were rolled {num_rolls} times")

    #   exit the program
        break

    # else
    else:

    #   print invalid input
        print("invalid input!")
