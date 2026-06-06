# Student Performance Analyzer

# -----------------------------------
# List of student marks

marks = [78, 45, 92, 35, 88, 40, 99, 56]

# -----------------------------------
# Passed students list

passed_students = []

# Failed students count

failed_count = 0

# Merit list

merit_list = []

# -----------------------------------
# Initialize highest and lowest marks

highest = marks[0]
lowest = marks[0]

# -----------------------------------
# Process marks

for mark in marks:

    # Passed students

    if(mark >= 40):
        passed_students.append(mark)
    else:
        failed_count = failed_count + 1

    # Highest marks

    if(mark > highest):
        highest = mark

    # Lowest marks

    if(mark < lowest):
        lowest = mark

    # Merit list

    if(mark > 75):
        merit_list.append(mark)

# -----------------------------------
# Display results

print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)