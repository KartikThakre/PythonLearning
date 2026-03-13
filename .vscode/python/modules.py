# The math module in Python provides various mathematical functions and constants. We will use the sqrt() function from the math module to calculate the square root of a number and print the result to the console.
import math
no = 16 
result = math.sqrt(no)
print("The square root of", no, "is", result)

# The random module in Python provides functions for generating random numbers. We will use the randint() function from the random module to generate a random integer between 1 and 100 and print it to the console.
import random
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# The datetime module in Python provides classes for manipulating dates and times. We will use the datetime class from the datetime module to get the current date and time and print it to the console.
from datetime import datetime
current_date_time = datetime.now()  
print("Current date and time:", current_date_time)

# Importing the functions module to use its functions for basic arithmetic operations. We will call the add, subtract, multiply, and divide functions with specific arguments and print the results to the console.
# This is built-in module in Python that provides various mathematical functions and constants. We will use the sqrt() function from the math module to calculate the square root of a number and print the result to the console.
import fuctions
print(fuctions.add(5, 3))
print(fuctions.subtract(5, 3))
print(fuctions.multiply(5, 3))
print(fuctions.divide(5, 3))

# This code imports the add, subtract, multiply, and divide functions directly from the fuctions module, allowing us to call them without the module prefix. We then call each function with specific arguments (5 and 3) and print the results to the console. This demonstrates how to use functions from an imported module in Python.
from fuctions import add, subtract, multiply, divide
print(add(5, 3))
print(subtract(5, 3))   
print(multiply(5, 3))
print(divide(5, 3))


import math
number = input("Enter a number : ")
result = math.sqrt(float(number))
result_one =math.pow(float(number), 2)
result_two = math.factorial(int(float(number)))
print(f"The square root of {number} is {result}")
print(f"The square of {number} is {result_one}")
print(f"The factorial of {number} is {result_two}")