actual_cost = float(input("please enter the actual product price: "))
sale_ammount = float(input("please enter the sales amount: "))

if (sale_ammount > actual_cost):
    ammount = sale_ammount - actual_cost
    print("total profit = ", ammount)
else:
    print("no profit")
