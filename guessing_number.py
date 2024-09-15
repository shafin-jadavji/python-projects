'''
Write a program to have the computer randomly select a number 
between 1 and 100, and then prompt the player to guess the number. 
The program should give hints if the guess is too high or too low. 
'''
# randomely generate number between min and max
# intialize number of trys to 0
# loop
    # prompt for guess
    # if valid guess between min and max
        # increment number of trys
        # if guess higher than number
            # print To High Try again
        # if guess lower than number
            # print To Low Try again
        # else
            # print Congratulations you got the number right in number of trys
            # exit loop
    # else
        # print Invalid input!
        # repeat loop

import random

min_num = 1
max_num = 100

random_num = random.randint(min_num, max_num)
num_trys = 0

while True:
    try:
        guess = int(input(f"Guess the number between {min_num} and {max_num}: "))
              
    except ValueError:
        print("Please enter a valid number!")
        continue
    # if valid guess isbetween min and max
    if min_num <= int(guess) <= max_num:
        num_trys += 1
        if guess < random_num:
            print("To low! Try again")
        elif guess > random_num:
            print("To high! Try again")
        else:
            print(f"Congratulations! You guessed the number in {num_trys} attempts")
            break
    else:
        print("Please enter a valid number!")
        continue
