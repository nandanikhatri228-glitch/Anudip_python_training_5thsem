'''An online store records orders as:
orders = [
 ("Laptop", 55000),
 ("Mouse", 800),
 ("Keyboard", 1500),
 ("Monitor", 12000),
 ("Pen Drive", 600)
]
Write a program to:
• Display all products costing more than ₹1000.
• Find the most expensive product.
• Calculate the total order value.
• Count products costing below ₹1000.'''
# Online Store Order Analysis

# -----------------------------------
# Orders list

orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# -----------------------------------
# Initialize variables

total_order_value = 0
below_1000_count = 0

most_expensive = orders[0]

# -----------------------------------
# Display products costing more than 1000

print("Products Costing More Than ₹1000:")

for order in orders:

    product_name = order[0]
    price = order[1]

    # Products above ₹1000

    if(price > 1000):
        print(product_name, "-", price)

    # Total order value

    total_order_value = total_order_value + price

    # Products below ₹1000

    if(price < 1000):
        below_1000_count = below_1000_count + 1

    # Most expensive product

    if(price > most_expensive[1]):
        most_expensive = order

# -----------------------------------
# Display results

print("\nMost Expensive Product:")
print(most_expensive[0], "-", most_expensive[1])

print("\nTotal Order Value:", total_order_value)

print("\nProducts Costing Below ₹1000:", below_1000_count)