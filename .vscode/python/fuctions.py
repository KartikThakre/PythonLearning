from colorama import init, Fore, Style
init(autoreset=True)        # enable colouring on Windows; reset after each print

# This code defines several functions for basic arithmetic operations (addition, subtraction, multiplication, and division) and a greeting function. The functions are then called with specific arguments to demonstrate their functionality, and the results are printed to the console. The division function also includes error handling for division by zero.
def greet():
    print("Hello! Welcome to Python programming.")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."    
greet()
print("Addition of 5 and 3 is:", add(5, 3)) 
print("Subtraction of 5 and 3 is:", subtract(5, 3))
print("Multiplication of 5 and 3 is:", multiply(5, 3))
print("Division of 5 and 3 is:", divide(5, 3))
print("Division of 5 and 0 is:", divide(5, 0))  

# This code defines several functions for basic arithmetic operations (addition, subtraction, multiplication, and division) and a greeting function. The functions are then called with specific arguments to demonstrate their functionality, and the results are printed to the console. The division function also includes error handling for division by zero.
def geet_greeting(name):
        return f"Hello, {name}! Welcome to Python programming." 
print(geet_greeting("Kartik"))

# This function takes a name as an argument and returns a personalized greeting message. We then call the function with the name "Kartik" and print the resulting greeting to the console.
def add_hours(monday, tuesday):
    total = monday + tuesday
    return total

result = add_hours(8, 9)

print("Total hours:", result)

# This function calculates the total and average hours worked in a week based on the hours provided for each day. It takes five parameters representing the hours worked from Monday to Friday, sums them up to get the total, and then divides by 5 to get the average. The function returns both the total and average hours as a tuple. We then call the function with specific hours for each day and print the results.
def weekly_hours(monday, tuesday, wednesday, thursday, friday):

    total = monday + tuesday + wednesday + thursday + friday
    average = total / 5

    return total, average


total, avg = weekly_hours(8,9,7,10,6)

print("Total:", total)
print("Average:", avg)


# This function takes a name as an argument and prints a greeting message. If no name is provided, it defaults to "Employee". The function is then called three times: once without an argument (which will use the default), and twice with specific names ("Kartik" and "Alice").
def greet(name="Employee"):
    print("Hello", name)

greet()
greet("Kartik")
greet("Alice")


def create_student(name, roll_no, **subjects):
    return {
        "name": name,
        "roll_no": roll_no,
        "subjects": subjects
    }


def calculate_result(student):
    marks = student["subjects"].values()

    total = sum(marks)
    avg = total / len(marks)

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "F"

    student["total"] = total
    student["average"] = avg
    student["grade"] = grade

    return student


   
def print_all_students(*students):
    # header in cyan
    print("\n" + Fore.CYAN + "================ STUDENT REPORT CARD ================")
    print(Fore.YELLOW + f"{'Name':<10}{'Roll':<6}{'Maths':<8}{'Science':<10}{'English':<10}{'Total':<8}{'Avg':<8}{'Grade':<6}")
    print(Fore.CYAN + "----------------------------------------------------------------")

    for s in students:
        # colour the grade depending on value
        grade = s['grade']
        if grade == 'A+':
            colour = Fore.GREEN
        elif grade in ('A','B'):
            colour = Fore.BLUE
        elif grade == 'C':
            colour = Fore.MAGENTA
        else:
            colour = Fore.RED
        print(f"{s['name']:<10}{s['roll_no']:<6}{s['subjects']['Maths']:<8}{s['subjects']['Science']:<10}{s['subjects']['English']:<10}{s['total']:<8}{round(s['average'],2):<8}" + colour + f"{grade:<6}")

    print("----------------------------------------------------------------")


def class_report(*students):
    total_avg = 0
    topper = students[0]
    passed = 0
    failed = 0

    for s in students:
        total_avg += s["average"]

        if s["average"] > topper["average"]:
            topper = s

        if s["grade"] == "F":
            failed += 1
        else:
            passed += 1

    class_avg = total_avg / len(students)

    return topper, class_avg, passed, failed


s1 = create_student("Kartik", 1, Maths=85, Science=90, English=88)
s2 = create_student("Rahul", 2, Maths=72, Science=75, English=70)
s3 = create_student("Aman", 3, Maths=55, Science=60, English=58)

calculate_result(s1)
calculate_result(s2)
calculate_result(s3)

print_all_students(s1)
print_all_students(s2)
print_all_students(s3)

topper, class_avg, passed, failed = class_report(s1, s2, s3)

print("\nClass Summary")
print("Topper:", topper["name"])
print("Class Average:", round(class_avg, 2))
print("Passed:", passed)
print("Failed:", failed)