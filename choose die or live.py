print("select your ride:")
print("1. bike")
print("2. car")

choice = int(input("Enter your choice : "))

if(choice == 1):
    print("what type of bike?")
    print("1. sports bike")
    print("2. cruiser bike")

    bike_choice = int(input("Enter your choice : "))

    if(bike_choice == 1):
        print("you have selected sports bike")
    elif(bike_choice == 2):
        print("you have selected cruiser bike")
    else:
        print("invalid choice for bike type")

elif(choice == 2):
    print("what type of car?")
    print("1. sedan")
    print("2. SUV")

    car_choice = int(input("Enter your choice : "))

    if(car_choice == 1):
        print("you have selected sedan")
    elif(car_choice == 2):
        print("you have selected SUV")
    else:
        print("invalid choice for car type")
else:
    print("invalid choice for ride type")