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

#UC4

print()
print("Enter 1 to check attendance status.")
print("Enter 2 to check full-day wages.")
print("Enter 3 to check part-time wages")
print()

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        check_attendance()
    case 2:
        fd_wages = full_day_wages()
        print("Your full-day wages are:", fd_wages)
    case 3:
        pt_wages = part_time_wages()
        print("Your part-time wages are:", pt_wages)
    case _:
        print("Please select from above choices only.")