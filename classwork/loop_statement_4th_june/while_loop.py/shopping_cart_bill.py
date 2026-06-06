# Shopping Cart Bill Calculator

# -----------------------------------
# Initialize total bill amount

total_bill = 0

# -----------------------------------
# Accept item prices until user enters 0

price = int(input("Enter Item Price: "))

while(price != 0):

    # Validation
    if(price < 0):
        print("Price should not be negative")

    else:
        total_bill = total_bill + price

    price = int(input("Enter Item Price: "))

# -----------------------------------
# Display total bill amount

print("Total Bill Amount:", total_bill)