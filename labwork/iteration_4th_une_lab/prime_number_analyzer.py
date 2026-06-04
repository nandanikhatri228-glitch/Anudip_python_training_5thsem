#Accept a number from the user and determine whether it is a prime number or not. 
number = int(input("Enter the number: "))

if number <= 0:
    print("Negative number should not be allowed")

elif number == 1:
    print("Not Prime")

else:
    count = 0

    print("Input:", number,"Output")
    print("Factors:", end=" ")

    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=" ")
            count += 1

    print()

    if count == 2:
        print(number, "is a Prime Number")
    else:
        print(number, "is not a Prime Number")
