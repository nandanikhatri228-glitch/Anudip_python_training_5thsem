# Inventory Stock Alert System

# -----------------------------------
# List of stock quantities

stock = [25, 5, 0, 12, 3, 18, 0, 30]

# -----------------------------------
# Initialize variables

out_of_stock = 0
available_products = 0

restock_required = []
healthy_stock = []

# -----------------------------------
# Process stock quantities

for quantity in stock:

    # Out of stock products

    if(quantity == 0):
        out_of_stock = out_of_stock + 1

    # Restock required

    if(quantity < 10):
        restock_required.append(quantity)

    # Available products

    if(quantity > 0):
        available_products = available_products + 1

    # Healthy stock

    if(quantity >= 15):
        healthy_stock.append(quantity)

# -----------------------------------
# Display results

print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock_required)
print("Available Products:", available_products)
print("Healthy Stock:", healthy_stock)