'''write the program to input the sentence
   and display the frequecnty of vowel
   which are present in the sentence ignoring the keys '''
# Program to count frequency of vowels

sentence = input("Enter a sentence: ")
# Initialize counters
a = e = i = o = u = 0

for ch in sentence:
    if ch == 'a' or ch == 'A':
        a += 1
    elif ch == 'e' or ch =='E':
        e += 1
    elif ch == 'i' or ch == 'I':
        i += 1
    elif ch == 'o' or ch == 'O':
        o += 1
    elif ch == 'u' or ch == 'U':
        u += 1
    
# Display frequency of vowel
print("Frequency of vowels:")
if ( a>0):
    print("a =", a)
if ( e>0):   
    print("e =", e)
if ( i>0):    
    print("i =", i)
if ( o>0):    
    print("o =", o)
if ( u>0):    
    print("u =", u)

            