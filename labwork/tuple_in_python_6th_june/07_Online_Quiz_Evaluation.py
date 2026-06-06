'''Correct answers: 
correct = ['A', 'C', 'B', 'D', 'A'] 
Student answers: 
student = ['A', 'B', 'B', 'D', 'C'] Write a program to: 
•	Calculate score.  
•	Display incorrectly answered question numbers.  
•	Count correct and wrong answers.  
•	Determine pass/fail (minimum 60%).  
'''
# Online Exam Evaluation System

# -----------------------------------
# Correct and student answers

correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

# -----------------------------------
# Initialize variables

correct_count = 0
wrong_count = 0

wrong_questions = []

# -----------------------------------
# Compare answers

for i in range(len(correct)):

    if(correct[i] == student[i]):

        correct_count = correct_count + 1

    else:

        wrong_count = wrong_count + 1

        wrong_questions.append(i + 1)

# -----------------------------------
# Calculate score percentage

score_percentage = (correct_count / len(correct)) * 100

# -----------------------------------
# Display results

print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)

print("Incorrectly Answered Question Numbers:", wrong_questions)

print("Score Percentage:", score_percentage, "%")

# -----------------------------------
# Determine pass/fail

if(score_percentage >= 60):

    print("Pass")

else:

    print("Fail")