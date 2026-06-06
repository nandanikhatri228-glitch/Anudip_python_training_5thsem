# Mountain Number Checker

# -----------------------------------
# Accept number from user

number = input("Enter a Number: ")

# -----------------------------------
# Assume number is not mountain

peak_found = False
is_mountain = True

# -----------------------------------
# Check digits

for i in range(1, len(number)):

    # Increasing part
    if(not peak_found):

        if(number[i] > number[i - 1]):
            continue

        elif(number[i] < number[i - 1]):
            peak_found = True

        else:
            is_mountain = False
            break

    # Decreasing part
    else:

        if(number[i] < number[i - 1]):
            continue

        else:
            is_mountain = False
            break

# -----------------------------------
# Check if mountain exists

if(peak_found and is_mountain):
    print("Mountain Number")
else:
    print("Not a Mountain Number")