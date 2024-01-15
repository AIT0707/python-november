# Write a for loop that prints all even numbers from 1 to 10.
for even in range (1,11): # we use range modul to use the range of numbers from which we need to find evens
    if even % 2 == 0:
        print(even)

# What is the purpose of the "if-elif-else" statement in Python? Provide an example.
''' When working with conditions and booleans we often use 'if statement'. 
"Elif statement" we use if previous condition if false and we ask to proceed with next condition.
"Else statement" we use if to process with action will be done if all previous conditions aren't True
'''

a = 100
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
