# Task 1️⃣ Description (IF):
# 1. Grade criteria:
    # If the student's grade is exactly 90, print: "Congratulations! You've earned a full scholarship to the Science Academy!"
grade=89
if grade==90:
    print("Congratulations! You've earned a full scholarship to the Science Academy!")

    # If the grade is greater than or equal to 80 and less than 90, print: "You qualify for admission to the Science Academy."
if grade>=80 and grade<90:
    print("You qualify for admission to the Science Academy.")

    # If the grade is less than 80, print: "Unfortunately, your grades don't meet the requirements for admission."
if grade<80:
    print("Unfortunately, your grades don't meet the requirements for admission.")

# 2. Age Criteria:
   #  If the student's age is exactly 18 years old, print: "You are just old enough to apply for the Science Academy!"
age=18
if age==18:
    print("You are just old enough to apply for the Science Academy!")

    # If the age is less than 18, print: "You're too young to apply for the Science Academy."
if age<18:
    print("You're too young to apply for the Science Academy.")

    #If the age is greater than 18, print: "You've surpassed the eligible age to apply for the Science Academy."
if age>18:
    print("You've surpassed the eligible age to apply for the Science Academy.")

# Task 2️⃣ Description (WHILE):
# 1. Generate a Secret Number:
    # Generate a random secret number between 1 and 20. Use random module (import random)
import random
print(random.randrange(1, 20))

# 2. Guessing Process:
    # The program will make random guesses within the range of 1 to 20.
    #If a guess matches the secret number, print: "Congratulations! The secret number is <secret_number>."
secret_number=random.randrange(1,20)
guess=random.randrange(1,20)
if guess==secret_number:
    txt="Congratulations! The secret number is {}."
    print (txt.format(secret_number))

# 3. Loop Termination:
    # Use a while loop to continue guessing until the correct number is found.
    # Terminate the loop once the secret number is correctly guessed using the break statement.
secret_number=random.randrange(1,20)
guess=random.randrange(1,20)
while guess!=secret_number:
    print (guess)
    break
guess=random.randrange(1,20)

