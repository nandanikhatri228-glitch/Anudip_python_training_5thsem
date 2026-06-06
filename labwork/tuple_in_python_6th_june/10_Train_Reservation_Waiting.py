'''Passenger records: 
passengers = [ 
    ("Anuj", "Confirmed"), 
    ("Rahul", "Waiting"), 
    ("Priya", "Confirmed"), 
    ("Amit", "Waiting"), 
    ("Neha", "Confirmed") 
] 
Write a program to: 
•	Display all waiting-list passengers.  
•	Count confirmed and waiting passengers.  
•	Find whether a specific passenger has a confirmed ticket.  
•	Create separate lists for confirmed and waiting passengers. 
'''
# Passenger Reservation Analysis

passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed_count = 0
waiting_count = 0

confirmed_list = []
waiting_list = []

print("Waiting List Passengers:")

for passenger in passengers:

    name = passenger[0]
    status = passenger[1]

    if(status == "Confirmed"):

        confirmed_count = confirmed_count + 1
        confirmed_list.append(name)

    else:

        print(name)

        waiting_count = waiting_count + 1
        waiting_list.append(name)

print("\nConfirmed Passengers:", confirmed_count)
print("Waiting Passengers:", waiting_count)

print("\nConfirmed List:", confirmed_list)
print("Waiting List:", waiting_list)

# Search passenger

search_name = input("\nEnter Passenger Name: ")

found = False

for passenger in passengers:

    if(passenger[0] == search_name and passenger[1] == "Confirmed"):

        found = True
        break

if(found):
    print("Confirmed Ticket Found")
else:
    print("Confirmed Ticket Not Found")