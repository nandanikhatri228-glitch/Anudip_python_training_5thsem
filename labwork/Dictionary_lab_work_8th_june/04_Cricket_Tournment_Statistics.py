'''----------------------------------------------------
Problem Statement: Cricket Tournament Statistics

Scenario
Runs scored by players in a tournament:

runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

Tasks
• Display players scoring more than 500 runs.
• Find the Orange Cap winner.
• Find the lowest scorer.
• Calculate total runs scored.
• Create a list of players scoring below 400.
• Count players scoring between 400 and 600 runs.

----------------------------------------------------'''

# creating a dictionary to store player runs

runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# --------------------------------------------------
# Display players scoring more than 500 runs

print("Players Scoring More Than 500 Runs :")

for player, run in runs.items():
    if run > 500:
        print(player)

# --------------------------------------------------
# Find the Orange Cap winner

dict_items = list(runs.items())

orange_cap_winner = dict_items[0][0]
highest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_runs:
        orange_cap_winner = item[0]
        highest_runs = item[1]

print("\nOrange Cap Winner :", orange_cap_winner,
      "(", highest_runs, ")", sep="")

# --------------------------------------------------
# Find the lowest scorer

lowest_scorer = dict_items[0][0]
lowest_runs = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_runs:
        lowest_scorer = item[0]
        lowest_runs = item[1]

print("\nLowest Scorer :", lowest_scorer,
      "(", lowest_runs, ")", sep="")

# --------------------------------------------------
# Calculate total runs scored

total_runs = 0

for run in runs.values():
    total_runs += run

print("\nTotal Tournament Runs :", total_runs)

# --------------------------------------------------
# Create a list of players scoring below 400

below_400 = []

for player, run in runs.items():
    if run < 400:
        below_400.append(player)

print("\nPlayers Scoring Below 400 :")
print(below_400)

# --------------------------------------------------
# Count players scoring between 400 and 600 runs

count = 0

for run in runs.values():
    if 400 <= run <= 600:
        count += 1

print("\nPlayers Between 400 and 600 Runs :", count)

# --------------------------------------------------

'''
Output:

Players Scoring More Than 500 Runs :
Virat
Rohit
Gill
Pant

Orange Cap Winner :Gill(698)

Lowest Scorer :Hardik(278)

Total Tournament Runs :4657

Players Scoring Below 400 :
['Hardik', 'Surya', 'Jadeja']

Players Between 400 and 600 Runs : 5
'''