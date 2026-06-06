# Number Mirror Check

# -----------------------------------
# Accept number from user

number = input("Enter a Number: ")

# -----------------------------------
# Check if number has even digits

if(len(number) % 2 != 0):

    print("Not a Mirror Number")

else:

    # -----------------------------------
    # Find middle position

    mid = len(number) // 2

    # -----------------------------------
    # Split number into two halves

    left_half = number[:mid]
    right_half = number[mid:]

    # -----------------------------------
    # Check mirror condition

    if(left_half == right_half):

        print("Mirror Number")

    else:

        print("Not a Mirror Number")