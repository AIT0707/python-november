# Create a simple number guessing game where the computer randomly selects a number, and the user tries to guess it.

"""
1. The computer selects a random number between 1 and 20 (inclusive).
2. Ask the user to guess the number.
3. Provide hints (higher/lower) based on the user's guess until they guess the correct number.
4. Count the number of attempts it takes the user to guess correctly.
5. Display a congratulatory message with the number of attempts when the user guesses the correct number.
"""

import random 
def guess_number_game():
    guess_number = random.randint(1,20) #to call random number in the range from 1 to 20
    attempts = 0 # to count amount of the attempts 
    while True:
        number = int(input("Guess the number (between 1 and 20): "))
        attempts += 1 # each will be counted until the number will be guessed
        if number < guess_number:
         print("Guessed number is low, try again.")
        elif number > guess_number:
         print("Guessed number is high, try again.")
        else:
         print(f"Congratulations! You guessed the number in {attempts} attempts.")
         break # once the number has been guessed game is over
guess_number_game()