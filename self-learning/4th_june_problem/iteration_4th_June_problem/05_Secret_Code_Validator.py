# Secret Code Validator

# -----------------------------------
# Accept secret code

code = input("Enter Secret Code: ")

# -----------------------------------
# Check if code contains exactly 6 digits

if(len(code) != 6 or not code.isdigit()):

    print("Invalid Code")

else:

    # -----------------------------------
    # Calculate sum of first 3 digits

    first_sum = int(code[0]) + int(code[1]) + int(code[2])

    # -----------------------------------
    # Calculate sum of last 3 digits

    last_sum = int(code[3]) + int(code[4]) + int(code[5])

    # -----------------------------------
    # Check validity

    if(first_sum == last_sum):

        print("Valid Code")

    else:

        print("Invalid Code")