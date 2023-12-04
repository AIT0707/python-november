import random
def guess_number_game():
    guess_number = random.randint(1,20)
    attempts = 0
    while True:
        number = int(input("Guess the number (between 1 and 20): "))
        attempts += 1
        if number < guess_number:
         print("Guessed number is low, try again.")
        elif number > guess_number:
         print("Guessed number is high, try again.")
        else:
         print(f"Congratulations! You guessed the number in {attempts} attempts.")
         break
guess_number_game()