'''Write a program to input a sentence from the user
and count the number of special characters present in the sentence'''
sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:
    if not ch.isalnum():
        count += 1

print("Number of special characters:", count)
