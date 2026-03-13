# ? Variables in Python and their datatypes
# Variables are used to store data in a program. They act as containers for values that can be used and manipulated throughout the code. In Python, you can create a variable by simply assigning a value to it using the equals sign (=). The type of the variable is determined by the value assigned to it. Here are some examples of different types of variables in Python:

# This variable represents the name of the person. It is a string value, which means it can contain letters, numbers, and special characters.
name = 'Kartik'
# This variable represents the age of the person. It is an integer value, which means it can only be a whole number without decimal points.
age = 25
# This variable represents the height of the person in centimeters. It is a floating-point number, which can have decimal values.
height = 175.5
# This variable indicates whether the person is a student or not. It is a boolean value, which can be either True or False.
is_student = True

# Now we will print the values of these variables to the console to see the output.
print("Name:", name)
print("Age:", age)  
print("Height:", height, "cm")
print("Is Student:", is_student)
# You can also use formatted strings (f-strings) to print the variables in a more readable way.
# The f-string allows you to embed expressions inside string literals, using curly braces {}. This makes it easier to format the output.
print(f"Hello {name}! You are {age} years old, {height} cm tall, and it is {is_student} that you are a student.")


# ? Numeric Variables
# Numeric variables are used to store numbers in Python. They can be of two main types: integers and floating-point numbers. Integers are whole numbers without a decimal point, while floating-point numbers can have decimal points. Here are some examples of numeric variables: 
mondy = 1000  # This variable represents the amount of money in dollars. It is an integer value.
pi = 3.14159  # This variable represents the value of pi. It is a floating-point number.    

total_cost = mondy * 2  # This variable calculates the total cost by multiplying the money variable by 2. It will be an integer value.
circumference = 2 * pi * 10  # This variable calculates the circumference of a circle with a radius of 10 using the formula C = 2 * π * r. It will be a floating-point number.
print("Money:", mondy)
print("Pi:", pi)
print("Total Cost:", total_cost)
print("Circumference:", circumference)


# ? String Variables
# String variables are used to store text in Python. They can contain letters, numbers, and special characters. Strings are enclosed in either single quotes (' ') or double quotes (" "). Here are some examples of string variables:
greeting = "Hello, World!"  # This variable represents a greeting message. It is a string value.
name = 'Alice'  # This variable represents a person's name. It is also a string value.
message = f"{greeting} My name is {name}."  # This variable combines the greeting and name variables into a single message using an f-string. It will be a string value.
print(greeting)
print(name)
print(message)


# ? Boolean Variables
# Boolean variables are used to store truth values in Python. They can only be either True or False. Boolean variables are often used in conditional statements and loops to control the flow of the program. Here are some examples of boolean variables:
is_raining = False  # This variable indicates whether it is raining or not. It is a boolean value.
is_sunny = True  # This variable indicates whether it is sunny or not. It is also a boolean value.
can_go_outside = not is_raining and is_sunny  # This variable determines if you can go outside based on the values of is_raining and is_sunny. It will be True if it is not raining and sunny, otherwise it will be False.
print("Is it raining?", is_raining)     
print("Is it sunny?", is_sunny)
print("Can I go outside?", can_go_outside)      


# ? List Variables
# List variables are used to store multiple values in a single variable. They are ordered, mutable (can be changed), and can contain elements of different types. Lists are defined using square brackets [] and the elements are separated by commas. Here are some examples of list variables:
fruits = ["apple", "banana", "cherry"]  # This variable represents a list of fruits. It is a list variable containing string values.
numbers = [1, 2, 3, 4, 5]  # This variable represents a list of numbers. It is a list variable containing integer values.
mixed_list = ["hello", 42, 3.14, True]  # This variable represents a list that contains different types of elements: a string, an integer, a floating-point number, and a boolean value. It is a list variable with mixed data types.
print("Fruits:", fruits)    
print("Numbers:", numbers)
print("Mixed List:", mixed_list)
print("First fruit:", fruits[0])  # This line prints the first element of the fruits list, which is "apple". List indexing starts at 0, so fruits[0] refers to the first element.   
print("Last number:", numbers[-1])  # This line prints the last element of the numbers list, which is 5. Using -1 as the index allows you to access the last element of the list regardless of its length.
print("Middle number:", numbers[len(numbers) // 2])  # This line prints the middle element of the numbers list, which is 3. The expression len(numbers) // 2 calculates the index of the middle element by dividing the length of the list by 2 using integer division.
print("Last 2nd number:", numbers[-2])  # This line prints the second to last element of the numbers list, which is 4. Using -2 as the index allows you to access the second to last element of the list.
print("Last 5th number:", numbers[-5]) # This line prints the fifth to last element of the numbers list, which is 1. Using -5 as the index allows you to access the fifth to last element of the list.
print("Last 3rd number:", numbers[-3]) # This line prints the third to last element of the numbers list, which is 3. Using -3 as the index allows you to access the third to last element of the list.
print("Numbers from index 1 to 3:", numbers[1:4])  # This line prints a slice of the numbers list from index 1 to index 3 (4 is exclusive), which will output [2, 3, 4]. List slicing allows you to access a range of elements in the list.
print("Every second number:", numbers[::2])  # This line prints every second element of the numbers list, which will output [1, 3, 5]. The slice notation [::2] means to start from the beginning of the list and take every second element.
print("Every element in normal order:", numbers[::1]) # This line prints the numbers list in normal order, which will output [1, 2, 3, 4, 5]. The slice notation [::1] means to start from the beginning of the list and take every element in the original order.
print("Reversed numbers:", numbers[::-1])
print("Is 'banana' in fruits?", "banana" in fruits)  # This line checks if the string "banana" is present in the fruits list and prints the result, which will be True. The 'in' keyword is used to check for membership in a list.
print("Length of mixed list:", len(mixed_list))  # This line prints the length of the mixed_list, which is 4. The len() function is used to get the number of elements in a list.
fruits.append("orange")  # This line adds the string "orange" to the end of the fruits list. The append() method is used to add an element to the end of a list.
print("Fruits after appending orange:", fruits)  # This line prints the updated fruits list, which now includes "orange". The output will be ['apple', 'banana', 'cherry', 'orange'].
numbers.remove(3)  # This line removes the first occurrence of the number 3 from the numbers list. The remove() method is used to remove a specific element from a list by value.
print("Numbers after removing 3:", numbers)  # This line prints the updated numbers list, which no longer contains the number 3. The output will be [1, 2, 4, 5].       
numbers[1] = 20  # This line updates the value at index 1 of the numbers list to 20. Since lists are mutable, you can change the values of existing elements by assigning a new value to a specific index.
print("Numbers after updating index 1 to 20:", numbers)  # This line prints the updated numbers list, which now has the value 20 at index 1. The output will be [1, 20, 4, 5].
print(len(numbers))  # This line prints the length of the numbers list, which is 4. The len() function is used to get the number of elements in a list. 
fruits.insert(1, "grape")  # This line inserts the string "grape" at index 1 of the fruits list. The insert() method is used to add an element at a specific index in a list, shifting the existing elements to the right.
print("Fruits after inserting grape at index 1:", fruits)  # This line prints the updated fruits list, which now includes "grape" at index 1. The output will be ['apple', 'grape', 'banana', 'cherry', 'orange'].
fruits.pop()  # This line removes the last element from the fruits list. The pop() method is used to remove and return the last element of a list. If you want to remove an element at a specific index, you can pass the index as an argument to pop(), like fruits.pop(1) to remove the element at index 1.
print("Fruits after popping the last element:", fruits)  # This line prints the updated fruits list after removing the last element, which will be ['apple', 'grape', 'banana', 'cherry'] since "orange" was removed by the pop() method.

# ? Itrating through a list
# You can iterate through a list using a for loop to access each element one by one.
for fruit in fruits:
    print(fruit)  # This line prints each fruit in the fruits list on a new line. The for loop iterates through each element in the list and assigns it to the variable 'fruit' in each iteration, allowing you to perform operations on it (in this case, printing it).

for no in numbers:
    print(no)  # This line prints each number in the numbers list on a new line. Similar to the previous loop, this for loop iterates through each element in the numbers list and assigns it to the variable 'no' in each iteration, allowing you to perform operations on it (in this case, printing it).

for i in range(len(fruits)):
    print(f"Index: {i}, Fruit: {fruits[i]}")  # This line prints the index and the corresponding fruit from the fruits list. The range(len(fruits)) generates a sequence of indices from 0 to the length of the fruits list minus one, allowing you to access each element by its index.

for i, fruit in enumerate(fruits):
    print(f"Index: {i}, Fruit: {fruit}")  # This line prints the index and the corresponding fruit from the fruits list using the enumerate() function. The enumerate() function adds a counter to an iterable and returns it as an enumerate object, which can be used in a for loop to get both the index and the value of each element in the list.

for i in range(0, len(fruits), 2):
    print(f"Index: {i}, Fruit: {fruits[i]}")  # This line prints every second fruit from the fruits list along with its index. The range(0, len(fruits), 2) generates a sequence of indices starting from 0 up to the length of the fruits list, with a step of 2, allowing you to access every second element in the list.

for i in range(len(fruits)-1, -1, -1):
    print(f"Index: {i}, Fruit: {fruits[i]}")  # This line prints the fruits in reverse order along with their indices. The range(len(fruits)-1, -1, -1) generates a sequence of indices starting from the last index of the fruits list down to 0, with a step of -1, allowing you to access the elements in reverse order.

# ? Unpacking Variables
# Unpacking variables is a convenient way to assign values from a list or tuple to multiple variables in a single line of code. It allows you to extract values from a sequence and assign them to individual variables without needing to access each element by index. Here are some examples of unpacking variables:
no = [1, 2, 3, 4, 5]
a,b,c,d,e = no
print(a)    
print(b)
print(c)    
print(d)
print(e)





# ? Dictionary Variables
# Dictionary variables are used to store key-value pairs in Python. They are unordered, mutable, and indexed by keys. Dictionaries are defined using curly braces {} and the key-value pairs are separated by commas. Here are some examples of dictionary variables:
person = {      
    "name": "Bob",  # This key-value pair represents the name of the person. The key is "name" and the value is "Bob".
    "age": 30,      # This key-value pair represents the age of the person. The key is "age" and the value is 30.
    "is_student": False  # This key-value pair indicates whether the person is a student or not. The key is "is_student" and the value is False.
}
print("Person:", person)
print("Name:", person["name"])  # This line prints the value associated with the key "name" in the person dictionary, which is "Bob". You can access values in a dictionary using their corresponding keys.
print("Age:", person["age"])  # This line prints the value associated with the key "age" in the person dictionary, which is 30.
print("Is Student?", person["is_student"])  # This line prints the value associated with the key "is_student" in the person dictionary, which is False.
person["age"] = 31  # This line updates the value associated with the key "age" in the person dictionary to 31. Since dictionaries are mutable, you can change the values of existing keys.
print("Updated Age:", person["age"])  # This line prints the updated value of the   "age" key in the person dictionary, which is now 31.
person["city"] = "New York"  # This line adds a new key-value pair  to the person dictionary, where the key is "city" and the value is "New York". You can add new key-value pairs to a dictionary by simply assigning a value to a new key.
print("Person with City:", person)  # This line prints the updated person dictionary, which now includes the new key-value pair for "city".

# storing multiple employees in a dictionary
employees = {
"E001": {"name": "Jordan", "hours": [8,9,7,10,6]},
"E002": {"name": "Alex", "hours": [7,8,8,9,8]}
}
print("Employees:", employees)
print("Employee E001 Name:", employees["E001"]["name"], employees["E001"]["hours"])  # This line prints the name of employee E001, which is "Jordan". You can access nested values in a dictionary by chaining the keys together.
print("Employee E002 Hours:", employees["E002"]["hours"])  # This line prints the hours worked by employee E002, which is [7, 8, 8, 9, 8].

# ? Iterating through a dictionary
# You can iterate through a dictionary using a for loop to access each key-value pair. Here
for emp_id, emp_info in employees.items():
    print(f"Employee ID: {emp_id}, Name: {emp_info['name']}, Hours: {emp_info['hours']}")  # This line prints the employee ID, name, and hours for each employee in the employees dictionary. The items() method returns a view object that displays a list of dictionary's key-value pairs, which can be used in a for loop to iterate through the dictionary.


# ? Tuple Variables
# Tuple variables are used to store multiple values in a single variable, similar to lists. However, tuples are immutable, which means that once they are created, their values cannot be changed. Tuples are defined using parentheses () and the elements are separated by commas. Here are some examples of tuple variables:
coordinates = (10.0, 20.0)  # This variable represents the coordinates of a point in a 2D space. It is a tuple variable containing two floating-point numbers.
person_info = ("Alice", 25, "Engineer")  # This variable represents a person's information, including their name, age, and profession. It is a tuple variable containing a string, an integer, and another string.
print("Coordinates:", coordinates)          
print("Person Info:", person_info)
print("Name:", person_info[0])  # This line prints the first element of the person_info tuple, which is "Alice". Tuple indexing starts at 0, so person_info[0] refers to the first element.
print("Age:", person_info[1])  # This line prints the second element of the person_info tuple, which is 25. person_info[1] refers to the second element of the tuple.
print("Profession:", person_info[2])  # This line prints the third element of the person_info tuple, which is "Engineer". person_info[2] refers to the third element of the tuple.
print("Coordinates Length:", len(coordinates))  # This line prints the length of the coordinates tuple, which is 2. The len() function is used to get the number of elements in a tuple.    
# coordinates[0] = 15.0  # This line will raise a TypeError because tuples are immutable and do not allow item assignment. You cannot change the values of a tuple once it has been created. If you need a mutable sequence, you should use a list instead of a tuple.
print("Updated Coordinates:", coordinates)  # This line will not be executed due to the error in the previous line. If you want to update the coordinates, you would need to create a new tuple with the desired values instead of trying to modify the existing one.
coordinates_one = (15.0, 25.0)  # This line creates a new tuple with the updated coordinates. Since tuples are immutable, we cannot change the existing tuple, but we can create a new one with the desired values.
print("New Coordinates:", coordinates_one)  # This line prints the new coordinates tuple, which is (15.0, 25.0).
print("Is coordinates the same as coordinates_one?", coordinates == coordinates_one)  # This line checks if the original coordinates tuple is the same as the new coordinates_one tuple and prints the result, which will be False since they contain different values. The '==' operator is used to compare the contents of two tuples for equality.
print("Is coordinates the same object as coordinates_one?", coordinates is coordinates_one)  # This line checks if the original coordinates tuple is the same object in memory as the new coordinates_one tuple and prints the result, which will also be False since they are two different tuples created at different times. The 'is' operator checks for identity, meaning it checks if both variables point to the same object in memory.
print("Coordinates Tuple:", coordinates)  # This line prints the original coordinates tuple, which is (10.0, 20.0). The original tuple remains unchanged because tuples are immutable.
print("New Coordinates Tuple:", coordinates_one[0])  # This line prints the new coordinates tuple, which is (15.0, 25.0). The new tuple was created to represent the updated coordinates since we cannot modify the original tuple.
employee = ("Kartik", 25)  # This line creates a tuple variable named employee that contains two elements: a string "Kartik" representing the name and an integer 25 representing the age. Tuples are defined using parentheses () and the elements are separated by commas.
# when you want the exact same value of name and age in different variables then we can use unpacking of tuple
name,age = employee
print(name)
print(age)



# ? Practise datatype
colors = ("red", "green", "blue","yellow" ,"orange")  # This line creates a tuple variable named colors that contains five string elements: "red", "green", "blue", "yellow", and "orange". Tuples are defined using parentheses () and the elements are separated by commas.
print(colors)  # This line prints the colors tuple, which will output ('red', 'green', 'blue', 'yellow', 'orange').
for color in colors:
    print("colors of the day:", color)  # This line prints each color in the colors tuple on a new line. The for loop iterates through each element in the tuple and assigns it to the variable 'color' in each iteration, allowing you to perform operations on it (in this case, printing it).
    print(len(color))  # This line prints the length of each color string in the colors tuple. The len() function is used to get the number of characters in each color string.
    print("access color by index:", colors.index(color))  # This line prints the index of each color in the colors tuple. The index() method is used to find the position of an element in a tuple.
    print("access color by slicing:", colors[colors.index(color)])  # This line prints each color in the colors tuple by accessing it through slicing. The expression colors[colors.index(color)] retrieves the color at the index found by the index() method, which will output the same color as the current iteration of the loop.
    print("access color by negative index:", colors[-(colors.index(color)+1)])  # This line prints each color in the colors tuple by accessing it through negative indexing. The expression colors[-(colors.index(color)+1)] retrieves the color at the negative index corresponding to its position in the tuple, which will also output the same color as the current iteration of the loop.

