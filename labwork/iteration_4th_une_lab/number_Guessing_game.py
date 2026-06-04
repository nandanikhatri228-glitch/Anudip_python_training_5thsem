#Generate a secret number between 1 and 50. 
secret_number = 25
attempts = 0

while True:
    guess = int(input("Enter a number between 1 and 50: "))

    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50")
        continue

    attempts += 1

    if guess > secret_number:
        print("Too High")

    elif guess < secret_number:
        print("Too Low")

    else:
        print("Correct Guess")
        print("Total Attempts:", attempts)
        break