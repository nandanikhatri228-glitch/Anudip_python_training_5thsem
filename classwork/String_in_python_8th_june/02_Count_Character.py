'''write a program and input a sentence from a user and count the number character present in it without using len function'''
str1 = input("Enter the sentence")
count = 0
for ch in str1:
    count+=1
print(count)