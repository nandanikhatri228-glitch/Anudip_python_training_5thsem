'''A company generates employee IDs in the following format: 
EMP2026ANUJ458 
Tasks 
Write a program to: 
1.	Count the number of uppercase letters.  
2.	Count the number of digits.  
3.	Extract the joining year.  
4.	Extract the employee name.  
5.	Check whether the ID follows these rules:  
o 	Starts with "EMP"  o 	Contains exactly 4 digits for the year  o 	Ends with exactly 3 digits  
6.	Create a list containing all digits present in the ID.  
7.	Find the sum of all digits present in the ID.  
8.	Display whether the ID is valid or invalid.  
'''
#----------------------------------------------------
#take the input from the user 
#employee id is divide into EMP,joining year,name of employee, number
emp_id = input("Enter Employee ID: ").strip()

# Validation 1
if not emp_id:
    exit("Employee ID cannot be empty")

# Extract parts once
prefix = emp_id[:3]
year = emp_id[3:7]
name = emp_id[7:-3]
emp_no = emp_id[-3:]

# Validation 2
if prefix != "EMP":
    exit("Employee ID must start with EMP")

# Validation 3
if len(year) != 4 or not year.isdigit():
    exit("Invalid Joining Year")

# Validation 4
if not name:
    exit("Employee Name cannot be empty")

# Validation 5
if len(emp_no) != 3 or not emp_no.isdigit():
    exit("Employee Number must contain exactly 3 digits")

print("-------------------------------------------------------")
print("Employee ID:", emp_id)
print("-------------------------------------------------------")

# 1. Count uppercase letters
upper_count = 0
for ch in emp_id:
    if ch.isupper():
        upper_count += 1

print("Uppercase Letters:", upper_count)

# 2. Count digits
digit_count = 0
for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

print("Digits:", digit_count)

# 3. Extract joining year
print("Joining Year:", year)

# 4. Extract employee name
print("Employee Name:", name)

print("-------------------------------------------------------")

# 5. Check ID rules
print("Starts with EMP:", prefix == "EMP")
print("Valid Year:", len(year) == 4 and year.isdigit())
print("Valid Employee Number:", len(emp_no) == 3 and emp_no.isdigit())

print("-------------------------------------------------------")

# 6. Create digit list
digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

print("Digit List:", digit_list)

# 7. Sum of digits
digit_sum = 0

for num in digit_list:
    digit_sum += num

print("Sum of Digits:", digit_sum)

print("-------------------------------------------------------")

# 8. ID Status
print("ID Status: Valid")