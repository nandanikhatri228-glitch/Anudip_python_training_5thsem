# Suspicious Transaction Detector

# -----------------------------------
# Initialize counters and total amount

high_transactions = 0
low_transactions = 0
total_amount = 0

# -----------------------------------
# Accept first transaction

amount = int(input("Enter Transaction Amount (-1 to Stop): "))

# -----------------------------------
# Repeat until -1 is entered

while(amount != -1):

    # Count transactions above ₹50,000

    if(amount > 50000):
        high_transactions = high_transactions + 1

    # Count transactions below ₹1,000

    if(amount < 1000):
        low_transactions = low_transactions + 1

    # Add to total amount

    total_amount = total_amount + amount

    # Accept next transaction

    amount = int(input("Enter Transaction Amount (-1 to Stop): "))

# -----------------------------------
# Display results

print("Transactions Above ₹50,000:", high_transactions)
print("Transactions Below ₹1,000:", low_transactions)
print("Total Transaction Amount: ₹", total_amount)