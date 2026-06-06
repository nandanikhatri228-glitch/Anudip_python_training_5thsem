'''Product IDs and quality status: 
products = [     (101, "Pass"), 
    (102, "Fail"), 
    (103, "Pass"), 
    (104, "Fail"), 
    (105, "Pass") 
] 
Write a program to: 
•	Display failed product IDs.  
•	Count passed and failed products.  
•	Calculate pass percentage.  
•	Stop checking if 3 failures are found.  
'''
# Product Quality Check System

products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

pass_count = 0
fail_count = 0

print("Failed Product IDs:")

for product in products:

    product_id = product[0]
    status = product[1]

    if(status == "Pass"):

        pass_count = pass_count + 1

    else:

        print(product_id)

        fail_count = fail_count + 1

        if(fail_count == 3):
            break

pass_percentage = (pass_count / len(products)) * 100

print("\nPassed Products:", pass_count)
print("Failed Products:", fail_count)

print("Pass Percentage:", pass_percentage, "%")