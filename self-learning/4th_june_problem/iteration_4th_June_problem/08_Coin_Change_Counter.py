# Coin Change Counter

# -----------------------------------
# Accept amount from user

amount = int(input("Enter Amount: "))

# -----------------------------------
# Validation

if(amount < 0):

    print("Amount should not be negative")

else:

    # -----------------------------------
    # Calculate notes

    note500 = amount // 500
    amount = amount % 500

    note200 = amount // 200
    amount = amount % 200

    note100 = amount // 100
    amount = amount % 100

    note50 = amount // 50
    amount = amount % 50

    note20 = amount // 20
    amount = amount % 20

    note10 = amount // 10
    amount = amount % 10

    # -----------------------------------
    # Display notes

    if(note500 > 0):
        print("500 x", note500)

    if(note200 > 0):
        print("200 x", note200)

    if(note100 > 0):
        print("100 x", note100)

    if(note50 > 0):
        print("50 x", note50)

    if(note20 > 0):
        print("20 x", note20)

    if(note10 > 0):
        print("10 x", note10)