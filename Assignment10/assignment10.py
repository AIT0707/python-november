"""
**Task1️⃣: Categorize Numbers in a List**

Create a Python program with a function named **`categorize_numbers()`** that takes in a list of numbers 
as an argument and categorizes each number based on conditions:

- If the number is greater than 10, print "High Number".
- If the number is between 5 and 10 (inclusive), print "Medium Number".
- If the number is less than 5, print "Low Number".

`number_list = [3, 7, 12, 5, 9]`
"""

def categorize_numbers(number_list):
 for number in number_list:
  if number>10:
   print("High number")
  elif number>=5 and number<=10:
   print("Medium Number")
  elif number<5:
   print("Low Number")
number_list=[3, 7, 12, 5, 9]
categorize_numbers(number_list)


"""
**Task2️⃣: Conditional Multiplication of Numbers in a List**

Create a Python program with a function named **`conditional_multiply()`** that takes in a list of numbers 
and a factor as arguments. This function should multiply each number in the list by the given factor 
but only if the number is greater than 5. If the number is 5 or less, it should print a message stating 
that the number is not multiplied.

`number_list = [3, 7, 12, 5, 9]`

`multiply_factor = 2`
"""

def conditional_multiply(number_list):
 for number in number_list:
  if number>5:
   print(number*multiply_factor)
  elif number<=5:
   print("The number is not multiplied")
number_list=[3, 7, 12, 5, 9]
multiply_factor=2
conditional_multiply(number_list)

 

   