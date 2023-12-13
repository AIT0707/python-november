def compare(): # Created a function
    number1 = input("Please enter number 1: ") 
    number2 = input("Please enter number 2: ")
    number3 = input("Please enter number 3: ")
    while True: # once the true condition is found the print commant wibll be run
        if number1>number2 and number1>number3:
            print("Number 1 is a largest number")
        elif number2>number1 and number2>number3:
            print("Number 2 is a largest number")
        elif number3>number1 and number3>number2:
            print("Number 3 is a largest number")
        break   
compare()