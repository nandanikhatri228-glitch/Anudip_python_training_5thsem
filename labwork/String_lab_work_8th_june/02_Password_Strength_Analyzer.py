'''Problem Statement A user enters a password. 
Python@2026! Tasks 
Write a program to determine whether the password is Strong, Medium, or Weak. 
Rules: 
•	Minimum length 8  
•	Contains at least:  
o	1 uppercase letter  o 	1 lowercase letter  o 	1 digit  
o	1 special character  Additionally: 
1.	Count uppercase letters.  
2.	Count lowercase letters.  
3.	Count digits.  
4.	Count special characters.  
5.	Display all digits separately.  
6.	Display all special characters separately.  
'''
# Take input
password = input("Enter Password: ").strip()

# Validation 1
if not password:
    exit("Password cannot be empty")
# Validation 2
if len(password) < 8:
    exit("Password must contain at least 8 characters")    

print("------------------------------------------")
print("Password:", password)
print("------------------------------------------")

'''1.	Count uppercase letters.  
   2.	Count lowercase letters.  
   3.	Count digits.  
   4.	Count special characters.  
'''
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

digit_list = []
special_list = []

# Traverse password
for ch in password:

    if ch.isupper():
        upper_count += 1

    elif ch.islower():
        lower_count += 1

    elif ch.isdigit():
        digit_count += 1
        digit_list.append(ch)

    else:
        special_count += 1
        special_list.append(ch)

# Display counts
print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

print("------------------------------------------")

# Display lists
print("Digits Found:", digit_list)
print("Special Characters Found:", special_list)

print("------------------------------------------")

# Password Strength
if (
    len(password) >= 8
    and upper_count >= 1
    and lower_count >= 1
    and digit_count >= 1
    and special_count >= 1
):
    print("Password Strength: Strong")

elif len(password) >= 8:
    print("Password Strength: Medium")

else:
    print("Password Strength: Weak")