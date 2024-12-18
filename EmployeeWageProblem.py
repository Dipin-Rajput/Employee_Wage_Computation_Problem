import random

#UC1

def welcome_message():
    print("Welcome to employee wage computation program.")

def check_attendance():
    attendance = random.choice([0, 1])
    if(attendance == 1):
        print("Employee is Present.")
        return attendance
    else:
        print("Employee is Absent.")
        return attendance

welcome_message()
status = check_attendance()

#UC2

wage_per_hour = 20
full_day_hours = 8

def calculate_daily_wage():

    if(status == 1):
        daily_wages = full_day_hours * wage_per_hour
        return daily_wages
    else:
        print("You are absent today.")

daily_wages = calculate_daily_wage()
print("Your today's wages:", daily_wages)

#UC3

part_time_hours = 8

def calculate_total_wage():

    if(status == 1):
        print("Enter 1 for part-time performed.")
        print("Enter 0 for part-time not performed.")
        part_time = int(input("Enter you input: "))

        if(part_time == 1):
            amount = daily_wages + part_time_hours * wage_per_hour
            print("Your today's wages are:", amount)
        else:
            wages = calculate_daily_wage()
            print("Your today's wages are:", wages)

calculate_total_wage()