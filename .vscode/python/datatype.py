name = "Kartik Thakre"
age = 25
height = 175.5  

# Now we will print the values of these variables along with their data types to the console.
# The type() function is used to determine the data type of a variable in Python. It returns the type of the variable as an output.
print(name , "is a", type(name), "and his age is", age, "which is of type", type(age), "and his height is", height, "which is of type", type(height))


a ="10"
b=5

# print(a + b)
# The above line will result in a TypeError because we are trying to add a string (a) and an integer (b). In Python, you cannot directly perform arithmetic operations between different data types without explicit conversion. To fix this, we need to convert the string '10' to an integer using the int() function before performing the addition. Similarly, if we want to perform floating-point addition, we can convert the string to a float using the float() function.
print(int(a) + b)
print(float(a) + b)


s = '42'
print (s, "is of type", type(s))
# The int() function is used to convert a string to an integer, and the float() function is used to convert a string to a floating-point number. This allows us to perform arithmetic operations on the string value by first converting it to a numeric type.
print (s * 2)
print (int(s) * 2)
# When we multiply a string by an integer, it repeats the string that many times. In this case, '42' * 2 will result in '4242'. However, when we convert the string to an integer using int(s) and then multiply it by 2, it will perform the arithmetic multiplication and give us 84 as the result.
print (int(s)/ 2)