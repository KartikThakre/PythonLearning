name = "Kartik"
roll_no = 1
marks = 85

print("Name:", name)
print("Roll No:", roll_no)  
print("Marks:", marks)


math = 85
science = 90
english = 88

marks_subject = math + science + english
average_marks = marks_subject / 3

print("Total Marks:", marks_subject)
print("Average Marks:", average_marks)


# input for marks for getting user input for marks of each subject and calculating total, average and grade based on the input marks.
enter_marks = input("Enter marks for Maths: ")
math = int(enter_marks)
enter_marks = input("Enter marks for Science: ")
science = int(enter_marks)
enter_marks = input("Enter marks for English: ")
english = int(enter_marks)

total_marks = math + science + english
average_marks = total_marks / 3

if average_marks >= 90:
    grade = "A+"
elif average_marks >= 80:
    grade = "A"
elif average_marks >= 70:
    grade = "B" 
elif average_marks >= 60:
    grade = "C" 
else:
    grade = "F"

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Grade:", grade)


number = input("Enter a number: ")
number = int(number)
if number % 2 == 0:
    print(number, "is an even number.") 
else:
    print(number, "is an odd number.")



number = int(input("Enter a number: "))
total = 0
for i in range(1, number + 1):
    total += i  
print("The sum of numbers from 1 to", number, "is:", total)



def calculate_salary(hours, rate):
    
    salary = hours * rate
    return salary   

print(calculate_salary(8,500))


hours = [8, 9, 7, 10, 6]
overtime_rate = 50
total_overtime_pay = 0  
overtime_days = 0   
for h in hours:
    if h > 8:
        overtime_hours = h - 8
        total_overtime_pay += overtime_hours * overtime_rate
        overtime_days += 1

print("Total Overtime Pay:", total_overtime_pay)    
print("Number of Overtime Days:", overtime_days)    


numbers = [12, 45, 7, 89, 23]
maxno = numbers[0]
for num in numbers:
    if num > maxno:
        maxno = num 
print("The largest number in the list is:", maxno)


student = {
"name": "Kartik",
"roll": 1,
"marks": 85
}

print("Name:", student["name"])
print("Roll No:", student["roll"])
print("Marks:", student["marks"])

import random
numbers = int(input("Enter a number: "))
random_number = random.randint(1, 10)
print(  f"Random number : {random_number}")