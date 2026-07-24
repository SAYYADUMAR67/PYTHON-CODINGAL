age = int(input("Enter your age: "))
 
if age >= 10:
    if age <= 20:
        print("The age is between 10 and 20 years.")
    else:
        print("The age is not between 10 and 20 years (it is greater than 20).")
else:
    print("The age is not between 10 and 20 years (it is less than 10).")