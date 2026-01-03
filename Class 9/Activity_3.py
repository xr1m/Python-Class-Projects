# Customise your ride:

choice = int(input("Enter your choice: 1 = Bike, 2 = Car: "))

if choice == 1:
    choice2 = int(input("Enter your choice: 1 = Scooter, 2 = Gear: "))
    if choice2 == 1:
        print("You've chosen scooter.")
    else:
        print("You've chosen gear.")
else:
    choice3 = int(input("Enter your choice: 1 = XUV, 2 = Sedan: "))
    if choice3 == 1:
        print("You've chosen an XUV.")
    else:
        print("You've chosen a Sedan.")
