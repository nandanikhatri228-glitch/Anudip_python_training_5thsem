'''A customer submits a review: 
This product is excellent excellent excellent and very useful 
Tasks 
Write a program to: 
1.	Count total words.  
2.	Create a dictionary containing word frequencies.  
3.	Find the most frequently used word.  
4.	Find all words appearing only once.  
5.	Count words having more than 5 characters.  
6.	Display words in reverse order.  
7.	Create a list of unique words.  
'''
# ----------------------------------------------------
# Take review input

review = input("Enter Review: ").strip()

# ----------------------------------------------------
# Validation 1

if not review:
    exit("Review cannot be empty")

# ----------------------------------------------------
# Convert review into words

word_list = review.split()

# Validation 2

if len(word_list) == 0:
    exit("Review must contain at least one word")

print("--------------------------------------------------")
print("Review:")
print(review)
print("--------------------------------------------------")

# ----------------------------------------------------
# 1. Count Total Words

total_words = len(word_list)

print("Total Words:", total_words)

print("--------------------------------------------------")

# ----------------------------------------------------
# 2. Create Word Frequency Dictionary

word_frequency = {}

for word in word_list:

    if word in word_frequency:
        word_frequency[word] += 1

    else:
        word_frequency[word] = 1

print("Word Frequencies:")
print(word_frequency)

print("--------------------------------------------------")

# ----------------------------------------------------
# 3. Find Most Frequently Used Word

most_frequent_word = ""
highest_frequency = 0

for word in word_frequency:

    if word_frequency[word] > highest_frequency:

        highest_frequency = word_frequency[word]
        most_frequent_word = word

print("Most Frequent Word:", most_frequent_word)

print("--------------------------------------------------")

# ----------------------------------------------------
# 4. Find Words Appearing Only Once

single_occurrence_words = []

for word in word_frequency:

    if word_frequency[word] == 1:
        single_occurrence_words.append(word)

print("Words Appearing Once:")
print(single_occurrence_words)

print("--------------------------------------------------")

# ----------------------------------------------------
# 5. Count Words Having More Than 5 Characters

long_word_count = 0

for word in word_list:

    if len(word) > 5:
        long_word_count += 1

print("Words Longer Than 5 Characters:", long_word_count)

print("--------------------------------------------------")

# ----------------------------------------------------
# 6. Display Words In Reverse Order

reverse_words = word_list[::-1]

print("Words In Reverse Order:")
print(reverse_words)

print("--------------------------------------------------")

# ----------------------------------------------------
# 7. Create List Of Unique Words

unique_words = []

for word in word_list:

    if word not in unique_words:
        unique_words.append(word)

print("Unique Words:")
print(unique_words)

'''Sample Output 
Total Words: 8 
 
Word Frequencies: 
This -> 1 product -> 1 is -> 1 excellent -> 3 
and -> 1 very -> 1 
useful -> 1 
 
Most Frequent Word: excellent 
 
Words Appearing Once: 
['This', 'product', 'is', 'and', 'very', 'useful'] 
 
Unique Words: 
['This', 'product', 'is', 'excellent', 'and', 'very', 'useful'] 
'''