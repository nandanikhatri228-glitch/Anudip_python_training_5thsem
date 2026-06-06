'''A batsman's scores in different matches are stored in a list. scores = [45, 78, 12, 100, 67, 8, 90, 55] Write a program to: 
•	Count half-centuries and centuries.  
•	Find the highest score.  
•	Display all scores below 20.  
•	Calculate the average score.  
'''
# Cricket Tournament Scorecard

# -----------------------------------
# Scores list

scores = [45, 78, 12, 100, 67, 8, 90, 55]

# -----------------------------------
# Initialize variables

half_centuries = 0
centuries = 0

highest_score = scores[0]

total_score = 0

print("Scores Below 20:")

# -----------------------------------
# Process scores

for score in scores:

    # Count half-centuries

    if(score >= 50 and score < 100):
        half_centuries = half_centuries + 1

    # Count centuries

    if(score >= 100):
        centuries = centuries + 1

    # Find highest score

    if(score > highest_score):
        highest_score = score

    # Display scores below 20

    if(score < 20):
        print(score)

    # Calculate total score

    total_score = total_score + score

# -----------------------------------
# Calculate average

average_score = total_score / len(scores)

# -----------------------------------
# Display results

print("\nHalf-Centuries:", half_centuries)
print("Centuries:", centuries)
print("Highest Score:", highest_score)
print("Average Score:", average_score)