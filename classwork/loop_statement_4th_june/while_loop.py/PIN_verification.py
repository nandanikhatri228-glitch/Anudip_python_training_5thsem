Enter_PIN = int(input("Enter your PIN: "))

while Enter_PIN != 1234:
    print("Incorrect PIN. Try Again.")
    Enter_PIN = int(input("Enter your PIN: "))

print("Enter PIN:", Enter_PIN ,"Access")
print("Granted")