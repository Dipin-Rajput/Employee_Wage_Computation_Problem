import random

#UC1

def welcome_message():
    print("Welcome to employee wage computation program.")

def check_attendance():
    attendance = random.choice([0, 1])
    if(attendance == 1):
        print("Employee is Present.")
    else:
        print("Employee is Absent.")

welcome_message()
check_attendance()