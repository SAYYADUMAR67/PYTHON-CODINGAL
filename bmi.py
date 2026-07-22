height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height/100) ** 2
print("Your BMI is",bmi)

if bmi < 18.4:
    print("You are underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
else:
    print("You are overweight.")