'''3.	Smart Parking System Problem Statement 
Parking slots are represented as: 
slots = [1, 0, 1, 1, 0, 0, 1, 0] 
Where: 
•	1 = Occupied  
•	0 = Available  Write a program to: 
•	Count occupied and available slots.  
•	Find the first available slot.  
•	Display all available slot numbers.  
•	Check whether parking occupancy exceeds 75%.  
'''
# Smart Parking System

# -----------------------------------
# Parking slots

slots = [1, 0, 1, 1, 0, 0, 1, 0]

# -----------------------------------
# Initialize variables

occupied_slots = 0
available_slots = 0

available_slot_numbers = []

first_available_slot = -1

# -----------------------------------
# Count occupied and available slots

for i in range(len(slots)):

    if(slots[i] == 1):

        occupied_slots = occupied_slots + 1

    else:

        available_slots = available_slots + 1

        available_slot_numbers.append(i + 1)

# -----------------------------------
# Find first available slot

for i in range(len(slots)):

    if(slots[i] == 0):

        first_available_slot = i + 1
        break

# -----------------------------------
# Calculate occupancy percentage

occupancy = (occupied_slots / len(slots)) * 100

# -----------------------------------
# Display results

print("Occupied Slots:", occupied_slots)
print("Available Slots:", available_slots)
print("First Available Slot:", first_available_slot)
print("Available Slot Numbers:", available_slot_numbers)
print("Occupancy Percentage:", occupancy, "%")

# -----------------------------------
# Check occupancy status

if(occupancy > 75):

    print("Parking Occupancy Exceeds 75%")

else:

    print("Parking Occupancy Does Not Exceed 75%")