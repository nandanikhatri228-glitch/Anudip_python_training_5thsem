# Consecutive Number Detector

# -----------------------------------
# List of numbers

numbers = [4, 5, 6, 10, 11, 15, 16, 17]

# -----------------------------------
# Create list for consecutive pairs

consecutive_pairs = []

# -----------------------------------
# Check consecutive numbers

for i in range(0, len(numbers)-1):

    if(numbers[i+1] == numbers[i] + 1):

        print(numbers[i], "and", numbers[i+1], "are consecutive")

        consecutive_pairs.append((numbers[i], numbers[i+1]))

# -----------------------------------
# Display consecutive pairs list

print("Consecutive Pairs:", consecutive_pairs)