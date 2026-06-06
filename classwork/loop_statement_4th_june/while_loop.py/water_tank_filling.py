#program that displays the amount of water in the tank after each minute and continues until the tank reaches 100 liters
tank_contain = 0
while tank_contain<100:
    tank_contain+=10
    print("Water Level:",tank_contain,"litres")
print("Tank is full.")    