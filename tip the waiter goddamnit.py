def tip_waiter(bill, tip_percentage):

    total= bill*(1 + 0.01*tip_percentage)
    total= round(total, 2)
    print(f"Please pay: ₹{total}")

tip_waiter(150, 30)