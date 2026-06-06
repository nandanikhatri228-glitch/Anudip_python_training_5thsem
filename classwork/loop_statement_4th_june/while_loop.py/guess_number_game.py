# Guess the Number Game

# -----------------------------------
# Secret number

secret_number = 7

# -----------------------------------
# Accept first guess from user

guess = int(input("Guess the Number: "))

# -----------------------------------
# Validation

if(guess < 0):
    print("Number should not be negative")

# -----------------------------------
# Repeat until correct guess

while(guess != secret_number):

    print("Wrong Guess. Try Again.")

    guess = int(input("Guess the Number: "))

# -----------------------------------
# Display success message

print("Congratulations! You guessed the correct number")
