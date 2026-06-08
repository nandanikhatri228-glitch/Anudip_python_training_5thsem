'''----------------------------------------------------
Problem Statement: Employee Performance Dashboard

Scenario
Employee performance scores are stored as:

performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

Tasks
• Display employees scoring above 80.
• Count employees needing improvement (score < 60).
• Find the top performer.
• Calculate average performance score.
• Create separate lists:
    - Excellent (≥ 90)
    - Good (75–89)
    - Average (60–74)
    - Poor (< 60)

----------------------------------------------------'''

# creating a dictionary to store employee performance scores

performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# --------------------------------------------------
# Display employees scoring above 80

print("Employees Scoring Above 80 :")
for emp_id, score in performance.items():
    if score > 80:
        print(emp_id)

# --------------------------------------------------
# Count employees needing improvement

improvement_count = 0

for score in performance.values():
    if score < 60:
        improvement_count += 1

print("\nEmployees Needing Improvement :", improvement_count)

# --------------------------------------------------
# Find the top performer

dict_items = list(performance.items())

top_performer = dict_items[0][0]
highest_score = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_score:
        top_performer = item[0]
        highest_score = item[1]

print("\nTop Performer :", top_performer,
      "(", highest_score, ")", sep="")

# --------------------------------------------------
# Calculate average performance score

total_score = 0

for score in performance.values():
    total_score += score

average_score = total_score / len(performance)

print("\nAverage Score :", round(average_score, 1))

# --------------------------------------------------
# Create separate lists

excellent = []
good = []
average = []
poor = []

for emp_id, score in performance.items():

    if score >= 90:
        excellent.append(emp_id)

    elif 75 <= score <= 89:
        good.append(emp_id)

    elif 60 <= score <= 74:
        average.append(emp_id)

    else:
        poor.append(emp_id)

# --------------------------------------------------
# Display categorized employee lists

print("\nExcellent :")
print(excellent)

print("\nGood :")
print(good)

print("\nAverage :")
print(average)

print("\nPoor :")
print(poor)

# --------------------------------------------------

'''
Output:

Employees Scoring Above 80 :
EMP101
EMP104
EMP105
EMP107

Employees Needing Improvement : 3

Top Performer : EMP105(97)

Average Score : 71.3

Excellent :
['EMP101', 'EMP105']

Good :
['EMP102', 'EMP104', 'EMP107']

Average :
['EMP108', 'EMP110']

Poor :
['EMP103', 'EMP106', 'EMP109']
'''