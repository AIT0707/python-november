# Scenario 1
num1 = 15.6
num2 = 8

#a. Add num1 and num2. Print the result.
print(num1+num2) # Output: 23.6

#or result can be also printed in integer data type
num1 = 15.6
num2 = 8
num3 = int(num1)
print(num2 + num3) # Output: 23

#b. Convert num2 to a floating-point number and multiply it with num1. Print the result.
num3 = float(num2) # Converted from int to float
print(num1 * num3) # Output: 124.8

"""
c. Explain the concept of type casting in Python and how it was used in these tasks.
The concept of type casting in Python is the process of convertiong a variable from one data type to another. 
In the 1st task the result has printed in both data types integer and float with adding third variable to convert the type from integer to float.
"""

# Scenario 2
message = "Hello, Python learners!"

#a. Print the length of the message.
print(len(message)) # Output: 23

#b. Convert the entire message to lowercase and print it. Done with using the lower method which returns the string in lower case.
print(message.lower()) # Output: 'hello, python learners!'

#c. Extract the word 'Python' from the message and print it separately. Done with using the slice syntax.
print (message[7:13]) # Output: 'Python'

#d. Explain the difference between methods like len() and lower() in Python and provide examples of their usage.
"""
len() and lower() are both built-in methods in Python, but they are used for different purposes.

len() is a function that returns the length of an object. 
For example, for a string s = "Winter is coming!", you can use len(s) to find the length of the string, which is 17.

lower() is a method that returns a copy of a string with all the alphabetic characters converted to lowercase. 
For example, if you have a string s = "I am fan of the FC Bayern Munchen!", you can use s.lower() to get a new string that is the same as s, 
but with all the alphabetic characters converted to lowercase: "i am fan of the fc bayern munchen!".
"""
