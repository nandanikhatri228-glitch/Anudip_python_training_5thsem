# Mini Employee Payroll System

# -----------------------------------
# Accept Employee Name

emp_name = input("Enter Employee Name: ")

# -----------------------------------
# Accept Basic Salary

basic_salary = float(input("Enter Basic Salary: "))

# -----------------------------------
# Validation

if(basic_salary < 0):
    print("Salary should not be negative")

else:

    # -----------------------------------
    # Calculate HRA, DA and PF

    hra = basic_salary * 20 / 100
    da = basic_salary * 10 / 100
    pf = basic_salary * 12 / 100

    # -----------------------------------
    # Calculate Gross Salary

    gross_salary = basic_salary + hra + da

    # -----------------------------------
    # Calculate Net Salary

    net_salary = gross_salary - pf

    # -----------------------------------
    # Determine Grade

    if(net_salary > 50000):
        grade = "Senior Grade"

    elif(net_salary > 30000):
        grade = "Mid Grade"

    else:
        grade = "Junior Grade"

    # -----------------------------------
    # Display Payroll Details

    print("\nEmployee Name:", emp_name)
    print("Basic Salary:", basic_salary)
    print("HRA:", hra)
    print("DA:", da)
    print("PF Deduction:", pf)
    print("Gross Salary:", gross_salary)
    print("Net Salary:", net_salary)
    print("Grade:", grade)