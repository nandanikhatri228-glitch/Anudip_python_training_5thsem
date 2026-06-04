#Accept a number from the user and check whether it is an Armstrong Number. 
number = int(input("enter the number"))
temp = number
sum =0
#validation
if(number<=0):
    print("negative number should not be allowed")
while temp>0:
    digit = temp%10
    sum = sum + digit **len(str(number))
    temp = temp//10
if sum ==number:
    if sum == number:
     print( "Input:",number, "Output:")
     print(number,"is an Armstrong Number")
else:
    print( "Input:",number, "Output:")
    print(number, "is not an Armstrong Number")
