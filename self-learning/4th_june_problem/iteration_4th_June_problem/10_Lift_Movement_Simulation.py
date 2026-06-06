# Lift Movement Simulation

# -----------------------------------
# Initial floor and total travelled

current_floor = 0
total_travelled = 0

# -----------------------------------
# Accept first destination

destination = int(input("Enter Destination (-1 to Stop): "))

# -----------------------------------
# Repeat until -1 is entered

while(destination != -1):

    # Calculate floors travelled

    if(destination > current_floor):
        travelled = destination - current_floor
    else:
        travelled = current_floor - destination

    # Display travelled floors

    print("Travelled:", travelled, "floors")

    # Update total travelled

    total_travelled = total_travelled + travelled

    # Update current floor

    current_floor = destination

    # Display current floor

    print("Current Floor:", current_floor)

    # Accept next destination

    destination = int(input("Enter Destination (-1 to Stop): "))

# -----------------------------------
# Display total floors travelled

print("Total Travelled:", total_travelled, "floors")