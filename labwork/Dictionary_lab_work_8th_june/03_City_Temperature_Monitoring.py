'''----------------------------------------------------
Problem Statement: City Temperature Monitoring System

Scenario
Daily temperatures of different cities are stored as:

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

Tasks
• Display cities having temperature above 40°C.
• Find the hottest city.
• Find the coolest city.
• Calculate average temperature.
• Create a list of pleasant cities (temperature < 35°C).
• Count cities with temperature between 35°C and 40°C.

----------------------------------------------------'''

# creating a dictionary to store city temperatures

temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# --------------------------------------------------
# Display cities having temperature above 40°C

print("Cities Above 40°C :")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

# --------------------------------------------------
# Find the hottest city

dict_items = list(temperature.items())

hottest_city = dict_items[0][0]
highest_temp = dict_items[0][1]

for item in dict_items:
    if item[1] > highest_temp:
        hottest_city = item[0]
        highest_temp = item[1]

print("\nHottest City :", hottest_city,
      "(", highest_temp, "°C)", sep="")

# --------------------------------------------------
# Find the coolest city

coolest_city = dict_items[0][0]
lowest_temp = dict_items[0][1]

for item in dict_items:
    if item[1] < lowest_temp:
        coolest_city = item[0]
        lowest_temp = item[1]

print("\nCoolest City :", coolest_city,
      "(", lowest_temp, "°C)", sep="")

# --------------------------------------------------
# Calculate average temperature

total_temperature = 0

for temp in temperature.values():
    total_temperature += temp

average_temperature = total_temperature / len(temperature)

print("\nAverage Temperature :",
      round(average_temperature, 1), "°C")

# --------------------------------------------------
# Create a list of pleasant cities

pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print("\nPleasant Cities :")
print(pleasant_cities)

# --------------------------------------------------
# Count cities with temperature between 35°C and 40°C

count = 0

for temp in temperature.values():
    if 35 <= temp <= 40:
        count += 1

print("\nCities Between 35°C and 40°C :", count)

# --------------------------------------------------

'''
Output:

Cities Above 40°C :
Delhi
Jaipur
Ahmedabad

Hottest City :Ahmedabad(43°C)

Coolest City :Bengaluru(28°C)

Average Temperature : 36.8 °C

Pleasant Cities :
['Mumbai', 'Bengaluru', 'Pune']

Cities Between 35°C and 40°C : 4
'''