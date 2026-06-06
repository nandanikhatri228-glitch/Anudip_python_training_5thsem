'''Employee data is stored as tuples:
employees = [
 ("Rahul", 35000),
 ("Priya", 55000),
 ("Amit", 42000),
 ("Neha", 65000)
]
Write a program to:
• Display employees earning above ₹50,000.
• Find the highest-paid employee.
• Calculate total salary expenditure.
• Count employees earning below ₹40,000. '''
# Employee Salary Analysis

# -----------------------------------
# Employee data

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# -----------------------------------
# Initialize variables

below_40000_count = 0

total_salary = 0

highest_paid = employees[0]

print("Employees Earning Above ₹50,000:")

# -----------------------------------
# Process employee records

for emp in employees:

    name = emp[0]
    salary = emp[1]

    # Employees earning above ₹50,000

    if(salary > 50000):
        print(name, "-", salary)

    # Find highest-paid employee

    if(salary > highest_paid[1]):
        highest_paid = emp

    # Calculate total salary expenditure

    total_salary = total_salary + salary

    # Count employees below ₹40,000

    if(salary < 40000):
        below_40000_count = below_40000_count + 1

# -----------------------------------
# Display results

print("\nHighest Paid Employee:")
print(highest_paid[0], "-", highest_paid[1])

print("\nTotal Salary Expenditure:", total_salary)

print("\nEmployees Earning Below ₹40,000:", below_40000_count)
