# Electricity Bill Simulator

# -----------------------------------
# Accept units consumed

units = int(input("Enter Units Consumed: "))

# -----------------------------------
# Validation

if(units < 0):
    print("Units should not be negative")

else:

    # -----------------------------------
    # Calculate bill according to slabs

    if(units <= 100):

        bill = units * 5

    elif(units <= 200):

        bill = (100 * 5) + ((units - 100) * 7)

    else:

        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    # -----------------------------------
    # Apply surcharge if bill exceeds ₹5000

    if(bill > 5000):

        surcharge = bill * 10 / 100

        final_bill = bill + surcharge

    else:

        surcharge = 0

        final_bill = bill

    # -----------------------------------
    # Display bill details

    print("Units Consumed:", units)
    print("Bill Amount: ₹", bill)
    print("Surcharge: ₹", surcharge)
    print("Final Payable Amount: ₹", final_bill)