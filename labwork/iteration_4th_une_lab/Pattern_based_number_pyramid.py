# Pattern Program
# Accept the number of rows and print:
# 1
# 12
# 123
# 1234
# 12345
# Also print the reverse pattern

# -----------------------------------
# Accept/Input the number of rows
rows = int(input("Enter the number of rows: "))

# -----------------------------------
# Validation
if(rows <= 0):
    print("Number of rows should be greater than 0")

# -----------------------------------
# Print the pattern
else:

    print("Pattern:")

    # Outer loop for rows
    for i in range(1, rows + 1, 1):

        # Inner loop for printing numbers
        for j in range(1, i + 1, 1):
            print(j, end="")

        # Move to next line
        print()

    # -----------------------------------
    # Print reverse pattern

    print("Reverse Pattern:")

    # Outer loop for reverse rows
    for i in range(rows, 0, -1):

        # Inner loop for printing numbers
        for j in range(1, i + 1, 1):
            print(j, end="")

        # Move to next line
        print()