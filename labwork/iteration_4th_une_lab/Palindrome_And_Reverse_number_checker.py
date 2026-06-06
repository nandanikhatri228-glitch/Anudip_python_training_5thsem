# Palindrome and Reverse Number Checker

# -----------------------------------
# Accept number from user

number = int(input("Enter a Number: "))

# Store original number

temp = number

# Initialize reverse number

reverse = 0

# -----------------------------------
# Reverse the number

while(number > 0):

    digit = number % 10

    reverse = (reverse * 10) + digit

    number = number // 10

# -----------------------------------
# Display reverse number

print("Reverse Number:", reverse)

# -----------------------------------
# Check palindrome

if(temp == reverse):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")