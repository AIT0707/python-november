# Define a function named calculate_area that takes the radius of a circle as a parameter and returns its area.

def calculate_circle_area(radius, pi): #Creating function with two arguments
    txt = "Circle ares is  {}" #Will present the result
    print(txt.format(pi*(int(radius))**2)) #Process of calculationf with selecting integer type for arguments

radius = input("Specify radius of circle: ") 
pi = 3.14

calculate_circle_area(radius, pi) #to run/order the function

# Explain the difference between parameters and arguments in a function.
# Parameter is how variable should be represented when it called and argument is a value of this variable

# Example 
def person (name, surname): # here name and surname are parameteres
    print (f"Hello, I am {name}, {surname}!")

person("James", "Bond") # here James and Bond are arguments