Enter_password = input("Enter your password: ")
while Enter_password != "admin123":
    print("Enter password:", Enter_password,"Invalid")
    print("Password.")
    Enter_password = input("Enter your password: ")

print("Enter password:", Enter_password,"Login")
print("Successful")