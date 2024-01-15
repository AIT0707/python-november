# Create a simple class called Car with attributes like make, model, and a method called start_engine.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start_engine(self):
        print("Engine will start in 3, 2, 1 . . .")

        car = Car("Audi", "RS8proline")
        print(f"The make of the car is {car.make} and the model is {car.model}")
        car.start_engine


# What is the significance of the __init__ method in a Python class?
# The main purpose of the _init_method is initiate all attributes included in the class by default. 