units = int(input("Enter the number of units consumed: "))

if (units < 50):
    bill = units * 2.60
    surcharge = 25

elif (units <= 100):
    bill = 130 + ((units - 50) * 3.25)
    surcharge = 35

elif (units <= 200):
    bill = 130 + 162.5 + ((units - 100) * 5.26)
    surcharge = 45

else:
    bill = 130 + 162.5 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total = bill + surcharge

print("/nElectricity Bill = %.2f"  %total)