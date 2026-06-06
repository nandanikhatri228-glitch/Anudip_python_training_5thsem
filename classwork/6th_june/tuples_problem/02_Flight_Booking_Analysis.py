# Flight Booking Analysis

# -----------------------------------
# Passenger booking records

bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# -----------------------------------
# Initialize variables

delhi_count = 0

confirmed_count = 0
waiting_count = 0
cancelled_count = 0

waiting_list = []

destination_count = {}

# -----------------------------------
# Display confirmed passengers

print("Confirmed Passengers:")

for booking in bookings:

    passenger_id = booking[0]
    destination = booking[1]
    status = booking[2]

    # Confirmed passengers

    if(status == "Confirmed"):
        print(passenger_id, destination)
        confirmed_count = confirmed_count + 1

    # Waiting passengers

    elif(status == "Waiting"):
        waiting_count = waiting_count + 1
        waiting_list.append(passenger_id)

    # Cancelled passengers

    elif(status == "Cancelled"):
        cancelled_count = cancelled_count + 1

    # Count Delhi passengers

    if(destination == "Delhi"):
        delhi_count = delhi_count + 1

    # Count destination bookings

    if(destination in destination_count):
        destination_count[destination] = destination_count[destination] + 1
    else:
        destination_count[destination] = 1

# -----------------------------------
# Find most booked destination

most_booked = ""
highest_count = 0

for destination in destination_count:

    if(destination_count[destination] > highest_count):

        highest_count = destination_count[destination]
        most_booked = destination

# -----------------------------------
# Display results

print("\nPassengers Travelling to Delhi:", delhi_count)

print("Confirmed:", confirmed_count)
print("Waiting:", waiting_count)
print("Cancelled:", cancelled_count)

print("\nWaiting List:")
print(waiting_list)

print("\nMost Booked Destination:")
print(most_booked)