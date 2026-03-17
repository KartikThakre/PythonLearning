# try:
#     num = int(input("Enter a number: "))
#     print(num)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")


# try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter another number: "))
#     result = a / b      
#     print(f"The result of {a} divided by {b} is: {result}")
# except ValueError:
#     print("Invalid input. Please enter valid integers.")    


# try:
#     age = int(input("Enter your age: "))
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     # valueError is raised when the user enters a negative age, and the error message "Age cannot be negative." is displayed. The except block catches the ValueError and prints the error message to the user, prompting them to enter a valid age.
# except ValueError as e:
#     print(f"Error: {e}")   


# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))
#     print(a / b)
# except ValueError:
#     print("Invalid number")
#     # ValueError is raised when the user enters a non-integer value for either a or b, and the error message "Invalid number" is displayed. The except block catches the ValueError and prints the error message to the user, prompting them to enter valid integers.
# except ZeroDivisionError:
#     print(f"Cannot divide by zero: {ZeroDivisionError}")


# try with else block is used to execute code that should run only if no exceptions were raised in the try block. In this example, if the user enters valid integers for a and b, the division will be performed and the result will be printed. If a ValueError occurs (e.g., if the user enters a non-integer), the except block will handle it and print "Invalid number". If a ZeroDivisionError occurs (e.g., if the user tries to divide by zero), the except block will handle it and print "Cannot divide by zero". The else block will only execute if no exceptions were raised, ensuring that the division result is printed only when valid input is provided.
# try:
#     num = int(input("Enter number: "))
# except ValueError:
#     print("Invalid input")
# else:
#     print("You entered:", num)


# The finally block is used to execute code that should run regardless of whether an exception was raised or not. In this example, the user is prompted to enter a number, and if they enter an invalid input (e.g., a non-integer), a ValueError will be raised and caught by the except block, which will print "Error". Regardless of whether an exception occurred or not, the finally block will execute and print "Program finished", ensuring that this message is always displayed at the end of the program's execution.
# try:
#     num = int(input("Enter number: "))
# except:
#     print("Error")
# finally:
#     print("Program finished")


# In this code snippet, the user is prompted to enter the number of hours worked. The input is then converted to an integer. If the user enters a value that cannot be converted to an integer (e.g., a non-numeric string), a ValueError will be raised, and the except block will catch it, printing "Please enter numeric value". If the input is successfully converted to an integer, the code checks if the hours are less than 0 or greater than 14. If either condition is true, it prints "Invalid hours". Otherwise, it prints "Hours recorded:" followed by the valid number of hours entered by the user.
# try:
#     hours = int(input("Enter hours worked: "))

#     if hours < 0 or hours > 14:
#         print("Invalid hours")
#     else:
#         print("Hours recorded:", hours)

# except ValueError:
#     print("Please enter numeric value")


# raise is used to manually trigger an exception in Python. In this code snippet, the user is prompted to enter the number of hours worked. The input is then converted to an integer. If the user enters a value that cannot be converted to an integer (e.g., a non-numeric string), a ValueError will be raised, and the except block will catch it, printing "Please enter numeric value". If the input is successfully converted to an integer, the code checks if the hours are less than 0. If this condition is true, it raises a ValueError with the message "Hours cannot be negative". The except block will catch this exception and print the error message to the user. If the hours are valid (i.e., not negative), it prints "Hours recorded:" followed by the valid number of hours entered by the user.
# hours = int(input("Enter hours: "))

# if hours < 0:
#     raise ValueError("Hours cannot be negative")   




# simple ANSI color constants (works in most modern terminals)
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"


def get_hours(day):
    try:
        h = int(input(f"{BLUE}Enter hours for {day}:{RESET} "))

        if h < 0 or h > 14:
            raise ValueError("Hours must be between 0 and 14")

        return h

    except ValueError:
        print(f"{RED}Invalid input. Please enter a number between 0 and 14.{RESET}")
        return None


def collect_employee():
    name = input(f"{BLUE}Enter employee name:{RESET} ")
    dept = input(f"{BLUE}Enter department:{RESET} ")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    hours = []

    for day in days:
        h = get_hours(day)

        if h is None:
            print(f"{RED}Error in input. Employee skipped.{RESET}\n")
            return None

        hours.append(h)

    return {
        "name": name,
        "dept": dept,
        "hours": hours
    }


def analyze_employee(emp):
    hours = emp["hours"]

    total = sum(hours)
    avg = total / 5

    overtime_days = 0
    for h in hours:
        if h > 8:
            overtime_days += 1

    if total < 30:
        status = "Underutilized"
    elif total <= 40:
        status = "Standard"
    else:
        status = "Heavy"

    emp["total"] = total
    emp["avg"] = avg
    emp["overtime_days"] = overtime_days
    emp["status"] = status

    return emp


def print_report(emp):
    print(f"\n{CYAN}----- Employee Report -----{RESET}")
    print(f"{GREEN}Name:{RESET}", emp["name"])
    print(f"{GREEN}Department:{RESET}", emp["dept"])
    print(f"{YELLOW}Hours:{RESET}", emp["hours"])
    print(f"{GREEN}Total Hours:{RESET}", emp["total"])
    print(f"{GREEN}Average:{RESET}", round(emp["avg"], 2))
    print(f"{GREEN}Overtime Days:{RESET}", emp["overtime_days"])
    print(f"{GREEN}Status:{RESET}", emp["status"])
    print(f"{CYAN}---------------------------{RESET}")


employees = []

n = int(input(f"{BLUE}How many employees?{RESET} "))

for i in range(n):
    print(f"\nEmployee {i+1}")
    emp = collect_employee()

    if emp:
        analyze_employee(emp)
        employees.append(emp)


for emp in employees:
    print_report(emp)