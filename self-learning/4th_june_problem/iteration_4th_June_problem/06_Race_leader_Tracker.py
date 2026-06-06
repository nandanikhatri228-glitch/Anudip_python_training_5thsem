# Race Leader Tracker

# -----------------------------------
# Accept number of racers

n = int(input("Enter Number of Racers: "))

# -----------------------------------
# Accept first racer's lap time

lap_time = float(input("Enter Lap Time of Racer 1: "))

fastest_time = lap_time
slowest_time = lap_time

fastest_position = 1
slowest_position = 1

# -----------------------------------
# Accept remaining lap times

for i in range(2, n + 1):

    lap_time = float(input("Enter Lap Time of Racer " + str(i) + ": "))

    # Check fastest racer

    if(lap_time < fastest_time):

        fastest_time = lap_time
        fastest_position = i

    # Check slowest racer

    if(lap_time > slowest_time):

        slowest_time = lap_time
        slowest_position = i

# -----------------------------------
# Calculate difference

difference = slowest_time - fastest_time

# -----------------------------------
# Display results

print("Fastest Racer Position:", fastest_position)
print("Slowest Racer Position:", slowest_position)
print("Difference Between Lap Times:", difference)