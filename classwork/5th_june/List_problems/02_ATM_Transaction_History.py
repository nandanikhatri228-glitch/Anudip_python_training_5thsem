# ATM Transaction History

# -----------------------------------
# List of transactions

transactions = [5000, -2000, 3000, -1000, -500, 7000]

# -----------------------------------
# Initialize variables

balance = 0

deposits = []
withdrawals = []

largest_deposit = 0
largest_withdrawal = transactions[1]

# -----------------------------------
# Process transactions

for transaction in transactions:

    # Calculate balance

    balance = balance + transaction

    # Deposits

    if(transaction > 0):

        deposits.append(transaction)

        if(transaction > largest_deposit):
            largest_deposit = transaction

    # Withdrawals

    elif(transaction < 0):

        withdrawals.append(transaction)

        if(transaction < largest_withdrawal):
            largest_withdrawal = transaction

# -----------------------------------
# Display results

print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)