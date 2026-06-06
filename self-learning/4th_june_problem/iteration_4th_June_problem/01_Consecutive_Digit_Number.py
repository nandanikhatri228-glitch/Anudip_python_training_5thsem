# Consecutive Number Checker

# -----------------------------------
# Accept number from user

number = int(input("Enter a Number: "))

# Store original number

temp = number

# Assume number is consecutive

is_consecutive = True

# -----------------------------------
# Check consecutive digits

while(number > 9):

    last_digit = number % 10
    previous_digit = (number // 10) % 10

    if(last_digit != previous_digit + 1):
        is_consecutive = False
        break

    number = number // 10

# -----------------------------------
# Display result

if(is_consecutive):
    print("Consecutive Number")
else:
    print("Not a Consecutive Number")