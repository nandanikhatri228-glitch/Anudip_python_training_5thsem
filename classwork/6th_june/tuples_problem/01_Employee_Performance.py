# Employee Performance Evaluation

# -----------------------------------
# Employee records stored in tuple

employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# -----------------------------------
# Employees scoring 80 or above

print("Employees Scoring 80 or Above:")

improvement_count = 0
high_performers = []

highest_employee = employees[0]

# -----------------------------------
# Process employee records

for emp in employees:

    emp_id = emp[0]
    emp_name = emp[1]
    score = emp[2]

    # Employees scoring 80 or above

    if(score >= 80):
        print(emp_id, emp_name, score)

    # Employees needing improvement

    if(score < 60):
        improvement_count = improvement_count + 1

    # Highest performer

    if(score > highest_employee[2]):
        highest_employee = emp

    # High performers list

    if(score > 75):
        high_performers.append(emp_name)

# -----------------------------------
# Display improvement count

print("\nEmployees Needing Improvement:", improvement_count)

# -----------------------------------
# Display highest performer

print("\nHighest Performer:")
print(highest_employee[0], highest_employee[1], highest_employee[2])

# -----------------------------------
# Display high performers

print("\nHigh Performers:")
print(high_performers)

# -----------------------------------
# Display performance categories

print("\nPerformance Categories:")

for emp in employees:

    score = emp[2]

    if(score >= 90):
        category = "Excellent"

    elif(score >= 75):
        category = "Good"

    elif(score >= 60):
        category = "Average"

    else:
        category = "Needs Improvement"

    print(emp[1], "->", category)