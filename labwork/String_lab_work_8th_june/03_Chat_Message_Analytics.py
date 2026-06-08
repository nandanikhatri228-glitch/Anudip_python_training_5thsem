'''A chat application stores a message: 
Python is awesome and Python is easy to learn 
Tasks 
Write a program to: 
1.	Count total characters.  
2.	Count total words.  
3.	Find the longest word.  
4.	Find the shortest word.  
5.	Count how many times the word "Python" appears.  
6.	Create a list of words having more than 4 characters.  
7.	Display all words starting with a vowel.  
8.	Count the number of vowels and consonants
'''
# ----------------------------------------------------
# Take message input from the user

message = input("Enter Message: ").strip()

# ----------------------------------------------------
# Validation 1

if not message:
    exit("Message cannot be empty")

# ----------------------------------------------------
# Convert message into list of words

word_list = message.split()

# Validation 2

if len(word_list) == 0:
    exit("Message must contain at least one word")

print("--------------------------------------------------")
print("Message:")
print(message)
print("--------------------------------------------------")

# ----------------------------------------------------
# 1. Count total characters

total_characters = len(message)
print("Total Characters:", total_characters)

# ----------------------------------------------------
# 2. Count total words

total_words = len(word_list)
print("Total Words:", total_words)

print("--------------------------------------------------")

# ----------------------------------------------------
# 3. Find longest word

longest_word = word_list[0]

for word in word_list:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest Word:", longest_word)

# ----------------------------------------------------
# 4. Find shortest word

shortest_word = word_list[0]

for word in word_list:
    if len(word) < len(shortest_word):
        shortest_word = word

print("Shortest Word:", shortest_word)

print("--------------------------------------------------")

# ----------------------------------------------------
# 5. Count occurrences of Python

python_count = 0

for word in word_list:
    if word == "Python":
        python_count += 1

print("Occurrences of Python:", python_count)

print("--------------------------------------------------")

# ----------------------------------------------------
# 6. Create list of words having more than 4 characters

long_words = []

for word in word_list:
    if len(word) > 4:
        long_words.append(word)

print("Words Longer Than 4 Characters:")
print(long_words)

print("--------------------------------------------------")

# ----------------------------------------------------
# 7. Display words starting with a vowel

vowel_words = []

for word in word_list:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("Words Starting With Vowel:")
print(vowel_words)

print("--------------------------------------------------")

# ----------------------------------------------------
# 8. Count vowels and consonants

vowel_count = 0
consonant_count = 0

for ch in message:

    if ch.isalpha():

        if ch.lower() in "aeiou":
            vowel_count += 1

        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

