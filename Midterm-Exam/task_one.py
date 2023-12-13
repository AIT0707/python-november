def calculate_triangle_area(base, height): #Creating function with two arguments
    txt = "Triangle ares is  {}" #Will present the result
    print(txt.format(0.5*(int(base))*(int(height)))) #Process of calculationf with selecting integer type for arguments

base = input("Specify base of triangle: ") 
height = input("Specify height of triangle: ")

calculate_triangle_area(base, height) #to run/order the function