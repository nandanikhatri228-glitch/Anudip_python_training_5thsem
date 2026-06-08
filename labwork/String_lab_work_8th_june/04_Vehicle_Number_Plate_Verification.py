'''A vehicle number plate is entered: 
MH12AB4589 
Tasks 
Write a program to: 
1.	Extract state code.  
2.	Extract district code.  
3.	Extract vehicle series.  
4.	Extract vehicle number.  
5.	Count letters and digits separately.  
6.	Verify:  
o	First 2 characters must be alphabets.  o 	Next 2 must be digits.  
o	Next 2 must be alphabets.  
o	Last 4 must be digits.  
7.	Display whether the number plate is valid.  
'''
# ----------------------------------------------------
# Take vehicle number input from user

vehicle_no = input("Enter Vehicle Number: ").strip()

# ----------------------------------------------------
# Validation 1: Empty Input

if not vehicle_no:
    exit("Vehicle Number cannot be empty")

# ----------------------------------------------------
# Validation 2: Length Check

if len(vehicle_no) != 10:
    exit("Vehicle Number must contain exactly 10 characters")

# ----------------------------------------------------
# Extract Parts

state_code = vehicle_no[:2]
district_code = vehicle_no[2:4]
series = vehicle_no[4:6]
vehicle_number = vehicle_no[6:]

# ----------------------------------------------------
# Validation 3: State Code

if not state_code.isalpha() or not state_code.isupper():
    exit("State Code must contain 2 uppercase letters")

# ----------------------------------------------------
# Validation 4: District Code

if not district_code.isdigit():
    exit("District Code must contain digits only")

# ----------------------------------------------------
# Validation 5: Vehicle Series

if not series.isalpha() or not series.isupper():
    exit("Vehicle Series must contain 2 uppercase letters")

# ----------------------------------------------------
# Validation 6: Vehicle Number

if not vehicle_number.isdigit():
    exit("Vehicle Number must contain digits only")

print("--------------------------------------------------")
print("Vehicle Number:", vehicle_no)
print("--------------------------------------------------")

# ----------------------------------------------------
# 1. Extract State Code

print("State Code:", state_code)

# ----------------------------------------------------
# 2. Extract District Code

print("District Code:", district_code)

# ----------------------------------------------------
# 3. Extract Vehicle Series

print("Series:", series)

# ----------------------------------------------------
# 4. Extract Vehicle Number

print("Vehicle Number:", vehicle_number)

print("--------------------------------------------------")

# ----------------------------------------------------
# 5. Count Letters and Digits

letter_count = 0
digit_count = 0

for ch in vehicle_no:

    if ch.isalpha():
        letter_count += 1

    elif ch.isdigit():
        digit_count += 1

print("Total Letters:", letter_count)
print("Total Digits:", digit_count)

print("--------------------------------------------------")

# ----------------------------------------------------
# 6. Verify Number Plate Format

print("State Code Valid:", state_code.isalpha() and state_code.isupper())

print("District Code Valid:", district_code.isdigit())

print("Series Valid:", series.isalpha() and series.isupper())

print("Vehicle Number Valid:", vehicle_number.isdigit())

print("--------------------------------------------------")

# ----------------------------------------------------
# 7. Display Final Status

print("Vehicle Number Status: Valid")


