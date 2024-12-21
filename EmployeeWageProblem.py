import random

#UC7

class EmployeeWageComputation:

    max_working_days = 20
    max_working_hours = 100

    def __init__(self, full_day_hours, part_time_hours, working_days_in_month, wage_per_hour):

        self.full_day_hours = full_day_hours
        self.part_time_hours = part_time_hours
        self.working_days_in_month = working_days_in_month
        self.wage_per_hour = wage_per_hour

    # Check Attendance

    def check_attendance(self):

        attendance = random.choice([0, 1])
        if(attendance == 1):
            print("Employee is Present.")
        else:
            print("Employee is Absent.")

        return attendance
    
    # Full-Day Wages

    def full_day_wages(self):

        status = self.check_attendance()
        daily_wages = None

        if(status == 1):
            daily_wages = full_day_hours * wage_per_hour
        
        return daily_wages
    
    # Part-Time Wages

    def part_time_wages(self):

        status = self.check_attendance()
        daily_wages = None

        if(status == 1):
            daily_wages = part_time_hours * wage_per_hour
        
        return daily_wages
    
    # Monthly Wages

    def monthly_wages(self):

        total_wages = 0

        for i in range(1, working_days_in_month + 1):

            full_day_status = self.check_attendance()

            if(full_day_status == 1):

                fd_wages = full_day_hours * wage_per_hour
                total_wages += fd_wages

                print(f"Your Day {i} full-day wages are:", fd_wages)

            else:
                print(f"Your Day {i} full-day wages are:", None)
            
            part_time_status = self.check_attendance()

            if(part_time_status == 1):

                pt_wages = part_time_hours * wage_per_hour
                total_wages += pt_wages

                print(f"Your Day {i} part-time wages are:", pt_wages)

            else:
                print(f"Your Day {i} part-time wages are:", None)

            print()
        
        return total_wages
    
    # Wages Based on Condition, Worked for less than 20 days and 100 hours

    def wages_with_conditions(self):

        total_days = 1
        total_hours = 0
        total_wages = 0

        while(total_hours < self.max_working_hours and total_days < self.max_working_days + 1):

            fd_status = self.check_attendance()

            if(fd_status == 1):

                hours_worked = full_day_hours
                total_hours += hours_worked
                total_wages += hours_worked * wage_per_hour

                print(f"Your Day {total_days} full-day wages are:", hours_worked * wage_per_hour)
            
            else:
                print(f"Your Day {total_days} full-day wages are:", None)
            
            pt_status = self.check_attendance()

            if(pt_status == 1):

                hours_worked = part_time_hours
                total_hours += hours_worked
                total_wages += hours_worked * wage_per_hour

                print(f"Your Day {total_days} part-time wages are:", hours_worked * wage_per_hour)

            else:
                print(f"Your Day {total_days} part-time wages are:", None)
            
            print()

            total_days += 1
        
        return total_wages


print("------------------------- Welcome to employee wage computation program -------------------------")
print()

full_day_hours = int(input("Enter your full-day hours: "))
part_time_hours = int(input("Enter your part-time hours: "))
working_days_in_month = int(input("Enter your working days in month: "))
wage_per_hour = int(input("Enter your wage per hour: "))

# max_working_hours = int(input("Enter your part-time hours: "))
# max_working_days = int(input("Enter your part-time hours: "))

emp_wage = EmployeeWageComputation(full_day_hours, part_time_hours, working_days_in_month, wage_per_hour)

first_exceution = True

while True:

    if(not first_exceution):

        print("------------------------- Enter yes to continue -------------------------")
        print("------------------------- Enter any key to exit -------------------------")
        print()
        repeat_choice = input("Do you want to continue ? : ")

        if(repeat_choice.capitalize() != "Yes"):
            print("Exiting the Program, Thank You for Joining.")
            break
    
    first_exceution = False

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
            emp_wage.check_attendance()
            print()
        case 2:
            print("Your full-day wages are:", emp_wage.full_day_wages())
            print()
        case 3:
            print("Your part-time wages are:", emp_wage.part_time_wages())
            print()
        case 4:
            print("Your monthly wages are:", emp_wage.monthly_wages())
            print()
        case 5:
            print("Your total wages based on condition are:", emp_wage.wages_with_conditions())
            print()
        case _:
            print("Please select from above choices only.")
            print()