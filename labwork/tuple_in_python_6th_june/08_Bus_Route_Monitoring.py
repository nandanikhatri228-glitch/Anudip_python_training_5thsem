'''Passenger count at each stop: 
passengers = [12, 18, 25, 30, 28, 15, 8] Write a program to: 
•	Find the busiest stop.  
•	Display stops with fewer than 10 passengers.  
•	Calculate average passengers.  
•	Determine whether any stop exceeded 25 passengers.  
'''
# Bus Passenger Analysis

# -----------------------------------
# Passenger count at each stop

passengers = [12, 18, 25, 30, 28, 15, 8]

# -----------------------------------
# Initialize variables

busiest_stop = 0
highest_passengers = passengers[0]

total_passengers = 0

print("Stops with Fewer Than 10 Passengers:")

# -----------------------------------
# Process passenger data

for i in range(len(passengers)):

    # Find busiest stop

    if(passengers[i] > highest_passengers):

        highest_passengers = passengers[i]
        busiest_stop = i

    # Display stops with fewer than 10 passengers

    if(passengers[i] < 10):

        print("Stop", i + 1, "-", passengers[i])

    # Calculate total passengers

    total_passengers = total_passengers + passengers[i]

# -----------------------------------
# Calculate average passengers

average_passengers = total_passengers / len(passengers)

# -----------------------------------
# Check if any stop exceeded 25 passengers

exceeded = False

for count in passengers:

    if(count > 25):

        exceeded = True
        break

# -----------------------------------
# Display results

print("\nBusiest Stop:", busiest_stop + 1)
print("Highest Passenger Count:", highest_passengers)

print("Average Passengers:", average_passengers)

if(exceeded):
    print("At least one stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")