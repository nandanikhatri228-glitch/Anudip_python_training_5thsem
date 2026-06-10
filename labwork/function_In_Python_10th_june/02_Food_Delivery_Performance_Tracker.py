# ==========================================================
# Food Delivery Performance Tracker
# ==========================================================
# Problem:
# Analyze delivery times of food orders using functions.
#------------------------------------------------------------
# Functions:
# 1. fastest_delivery(times)
# 2. delayed_orders(times)
# 3. average_delivery_time(times)
# 4. delivery_category(times)
# ==========================================================


# List containing delivery times of different orders
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]


# ==========================================================
# Function 1: Find Fastest Delivery
# Returns the minimum delivery time
# ==========================================================
def fastest_delivery(times):

    # Assume first delivery time is the fastest
    fastest = times[0]

    # Compare every delivery time
    for time in times:

        if time < fastest:
            fastest = time

    return fastest


# ==========================================================
# Function 2: Find Delayed Orders
# Returns orders taking more than 45 minutes
# ==========================================================
def delayed_orders(times):

    delayed_list = []

    for time in times:

        if time > 45:
            delayed_list.append(time)

    return delayed_list


# ==========================================================
# Function 3: Calculate Average Delivery Time
# Returns average delivery time
# ==========================================================
def average_delivery_time(times):

    total_time = 0

    # Calculate total delivery time
    for time in times:
        total_time += time

    # Calculate average
    average = total_time / len(times)

    return average


# ==========================================================
# Function 4: Display Delivery Categories
# Fast    -> <= 30 minutes
# Normal  -> 31 to 45 minutes
# Delayed -> > 45 minutes
# ==========================================================
def delivery_category(times):

    print("\nDelivery Categories")
    print("-" * 30)

    for time in times:

        if time <= 30:
            category = "Fast"

        elif time <= 45:
            category = "Normal"

        else:
            category = "Delayed"

        print(time, "->", category)


# ==========================================================
# Main Program
# ==========================================================

# Display fastest delivery
print("Fastest Delivery:",
      fastest_delivery(delivery_time),
      "minutes")

print()

# Display delayed orders
print("Delayed Orders:")
print(delayed_orders(delivery_time))

print()

# Display average delivery time
print("Average Delivery Time:")
print(round(
    average_delivery_time(delivery_time),
    2
), "minutes")

# Display delivery categories
delivery_category(delivery_time)
'''Sample Output

Fastest Delivery: 18 minutes

Delayed Orders:
[60, 80, 55]

Average Delivery Time:
40.8 minutes

Categories:
28 -> Fast
45 -> Normal
60 -> Delayed
...'''