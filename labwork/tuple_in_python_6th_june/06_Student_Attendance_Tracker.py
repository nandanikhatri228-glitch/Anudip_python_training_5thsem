'''Attendance for 15 days is recorded as: 
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P'] 
Write a program to: 
•	Count present and absent days.  
•	Calculate attendance percentage.  
•	Determine eligibility (minimum 75% attendance).  
•	Display positions where the student was absent.  
'''
# Student Attendance Analysis

# -----------------------------------
# Attendance record

attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# -----------------------------------
# Initialize variables

present_count = 0
absent_count = 0

absent_positions = []

# -----------------------------------
# Count attendance

for i in range(len(attendance)):

    if(attendance[i] == 'P'):

        present_count = present_count + 1

    else:

        absent_count = absent_count + 1

        absent_positions.append(i + 1)

# -----------------------------------
# Calculate attendance percentage

attendance_percentage = (present_count / len(attendance)) * 100

# -----------------------------------
# Display results

print("Present Days:", present_count)
print("Absent Days:", absent_count)

print("Attendance Percentage:", attendance_percentage, "%")

# -----------------------------------
# Check eligibility

if(attendance_percentage >= 75):

    print("Eligible")

else:

    print("Not Eligible")

# -----------------------------------
# Display absent positions

print("Absent Positions:", absent_positions)
