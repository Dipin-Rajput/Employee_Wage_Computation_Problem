import random

#UC1

def welcome_message():
    print("------------------------- Welcome to employee wage computation program -------------------------")

def check_attendance():
    attendance = random.choice([0, 1])
    if(attendance == 1):
        print("Employee is Present.")
        return attendance
    else:
        print("Employee is Absent.")
        return attendance

print()
welcome_message()
# check_attendance()

#UC2

wage_per_hour = 20
full_day_hours = 8

def full_day_wages():

    status = check_attendance()

    if(status == 1):
        daily_wages = full_day_hours * wage_per_hour
        return daily_wages
    else:
        return None

# fd_wages = full_day_wages()
# print("Your full-day wages are:", fd_wages)

#UC3

part_time_hours = 8

def part_time_wages():

    status = check_attendance()

    if(status == 1):
        daily_wages = part_time_hours * wage_per_hour
        return daily_wages
    else:
        return None

# pt_wages = part_time_wages()
# print("Your part-time wages are:", pt_wages)

#UC5

working_day_in_month = 20

def monthly_wages():

    total_wages = 0

    for i in range(1, working_day_in_month + 1):

        full_day_status = check_attendance()

        if(full_day_status == 1):

            fd_wages = full_day_hours * wage_per_hour
            total_wages += fd_wages

            print(f"Your Day {i} full-day wages are:", fd_wages)

        else:
            print(f"Your Day {i} full-day wages are:", None)
        
        part_time_status = check_attendance()

        if(part_time_status == 1):

            pt_wages = part_time_hours * wage_per_hour
            total_wages += pt_wages

            print(f"Your Day {i} part-time wages are:", pt_wages)

        else:
            print(f"Your Day {i} part-time wages are:", None)

        print()
    
    return total_wages

#UC6

max_working_hours = 100
max_working_days = 20

def wages_with_conditions():

    total_days = 1
    total_hours = 0
    total_wages = 0

    while(total_hours < max_working_hours and total_days < max_working_days + 1):

        fd_status = check_attendance()

        if(fd_status == 1):

            hours_worked = full_day_hours
            total_hours += hours_worked
            total_wages += hours_worked * wage_per_hour

            print(f"Your Day {total_days} full-day wages are:", hours_worked * wage_per_hour)
        
        else:
            print(f"Your Day {total_days} full-day wages are:", None)
        
        pt_status = check_attendance()

        if(pt_status == 1):

            hours_worked = random.randrange(1, 9)
            total_hours += hours_worked
            total_wages += hours_worked * wage_per_hour

            print(f"Your Day {total_days} part-time wages are:", hours_worked * wage_per_hour)

        else:
            print(f"Your Day {total_days} part-time wages are:", None)
        
        print()

        total_days += 1
    
    return total_wages

#UC4

print()
print("Enter 1 to check attendance status.")
print("Enter 2 to check full-day wages.")
print("Enter 3 to check part-time wages.")
print("Enter 4 to check monthly wages.")
print("Enter 5 to check wages based on condition of 100 hours and 20 days.")
print()

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        check_attendance()
    case 2:
        print("Your full-day wages are:", full_day_wages())
    case 3:
        print("Your part-time wages are:", part_time_wages())
    case 4:
        print("Your monthly wages are:", monthly_wages())
    case 5:
        print("Your total wages based on condition are:", wages_with_conditions())
    case _:
        print("Please select from above choices only.")

