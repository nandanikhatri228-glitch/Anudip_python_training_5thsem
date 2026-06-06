# Banking System Program

# -----------------------------------
# Initial Balance

balance = 10000

# -----------------------------------
# Repeat until Exit is selected

while(True):

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    # -----------------------------------
    # Check Balance

    if(choice == 1):
        print("Current Balance: ₹", balance)

    # -----------------------------------
    # Deposit Amount

    elif(choice == 2):

        amount = int(input("Enter Deposit Amount: "))

        if(amount > 0):
            balance = balance + amount
            print("Amount Deposited Successfully")
            print("Updated Balance: ₹", balance)

        else:
            print("Invalid Amount")

    # -----------------------------------
    # Withdraw Amount

    elif(choice == 3):

        amount = int(input("Enter Withdrawal Amount: "))

        if(amount > balance):
            print("Insufficient Balance")

        elif(amount <= 0):
            print("Invalid Amount")

        else:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance: ₹", balance)

    # -----------------------------------
    # Exit

    elif(choice == 4):

        print("Thank You For Using Banking System")
        break

    # -----------------------------------
    # Invalid Choice

    else:
        print("Invalid Choice. Please Try Again.")