distance =int(input("What is the distance(km)?"))
if distance < 3:
    print("Walk")
elif 3 <= distance <= 15:
    print("Bike")
else:
    print("Car")