#program to check whether a given number is a Strong Number
number = int(input("Enter a number: "))
#validation of number
temp = number
sum = 0
while temp > 0:
    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    sum = sum + fact
    temp = temp // 10

if sum == number:
    print("Input:",number, "Output")
    print(number,"is a Strong Number")
else:
    print("Input:",number, "Output")
    print(number, "is not a Strong Number")