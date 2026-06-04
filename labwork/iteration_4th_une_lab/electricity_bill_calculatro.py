#electricity bill 
unit = int(input("enter the unit consumed"))
#validation of input
if (unit<0):
    print("electricity unit should not be negative")
#--------------------------------------------
# calculation for bills 
# calculation  of bill when unit is between 0 to 100    
elif(unit<=100):
    bill = unit*5
    category = "Low Consumption"
#calculation of bill when unit is between 101 to 200    
elif(unit<=200):
    bill = (100*5)+((unit-100)*7)
    category = "Medium Consumption"
#calculation of bill when unit is more than 200    
else:
    bill = (100*5)+(100*7)+((unit-200)*10)
    category = "High Consumption"
print("Units Consumed:",unit)
print("Total Bill:",bill)
print("Category:",category)
