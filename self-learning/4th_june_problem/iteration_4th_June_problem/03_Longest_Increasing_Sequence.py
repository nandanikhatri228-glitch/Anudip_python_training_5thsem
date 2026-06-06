# Longest Increasing Sequence

# -----------------------------------
# Accept number of elements

n = int(input("Enter Number of Elements: "))

# -----------------------------------
# Accept first number

num = int(input("Enter Number: "))

current_length = 1
max_length = 1

# -----------------------------------
# Accept remaining numbers

for i in range(2, n + 1):

    next_num = int(input("Enter Number: "))

    # Check increasing sequence

    if(next_num > num):
        current_length = current_length + 1

    else:
        current_length = 1

    # Update maximum length

    if(current_length > max_length):
        max_length = current_length

    num = next_num

# -----------------------------------
# Display result

print("Longest Sequence Length =", max_length)