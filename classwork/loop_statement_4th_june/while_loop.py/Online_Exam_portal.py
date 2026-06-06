# Online Assessment Program

# -----------------------------------
# Accept first marks from user

marks = int(input("Enter Marks: "))

# -----------------------------------
# Validation

if(marks < 0):
    print("Marks should not be negative")

# -----------------------------------
# Repeat until student passes

while(marks < 40):

    print("Result: Fail")

    marks = int(input("Enter Marks: "))

# -----------------------------------
# Display pass message

print("Result: Pass")
print("Congratulations! You have cleared the assessment")