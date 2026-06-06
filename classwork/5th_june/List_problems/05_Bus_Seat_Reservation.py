# Bus Seat Reservation Analysis

# -----------------------------------
# List of seats

seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]

# -----------------------------------
# Initialize variables

booked_seats = 0
available_seats = 0

available_seat_numbers = []

first_available_seat = -1

# -----------------------------------
# Count seats and find first available seat

for i in range(len(seats)):

    if(seats[i] == 1):

        booked_seats = booked_seats + 1

    else:

        available_seats = available_seats + 1

        available_seat_numbers.append(i + 1)

# -----------------------------------
# Find first available seat

for i in range(len(seats)):

    if(seats[i] == 0):

        first_available_seat = i + 1
        break

# -----------------------------------
# Calculate occupancy percentage

occupancy = (booked_seats / len(seats)) * 100

# -----------------------------------
# Display results

print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)
print("First Available Seat:", first_available_seat)
print("Available Seat Numbers:", available_seat_numbers)
print("Bus Occupancy:", occupancy, "%")

if(occupancy > 70):

    print("Status: More Than 70% Occupied")

else:

    print("Status: Not More Than 70% Occupied")