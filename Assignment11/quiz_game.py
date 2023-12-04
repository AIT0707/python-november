# Create a fun quiz game in Python that asks easy questions and checks if the user's answers are correct.

"""
**Instructions:**

1. Show the user simple questions one by one.
2. Ask the user to type their answer for each question.
3. Check if the user's answer is correct.
4. Keep track of the user's score (how many correct answers they get).
5. Show the final score at the end of the quiz.
"""

score = 0

# Question 1
answer = input("What is the capital of Great Britain? ")
if answer == "London":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 2
answer = input("How many months are in the year? ")
if answer == "12":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 3
answer = input("When was COVID-19 find out (year)? ")
if answer == "2019":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 4
answer = input("What is 3 * 11? ")
if answer == "33":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 5
answer = input("What year did Worl War 2 end? ")
if answer.lower() == "1945":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

print(f"Your final score is {score} out of 5.")