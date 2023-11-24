'''
a. Create a program that demonstrates the use of logical operators (AND, OR, NOT)
on boolean values (assign boolean values directly in the code). 
Show the result of applying these operators.
'''

# With AND operator
print(12<15 and 12>10) # Output: True - because 12 is less than 15 and greater than 10

# With OR operator
print(13>8 or 13<9) # Output: True - because 13 is greater than 8 but it is not less than 9

# With NOT operator
print(not(13==13 and 13<25)) # Output: False - because we reversed result with NOT operator
