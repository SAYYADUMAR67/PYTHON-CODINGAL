class computerprice:
    def __init__(self):
        self.__holymaxprice = 25000
    def sell(self):
        print("this is your holy price 25000",self.__holymaxprice)
    def set_holy_ultra_pro_max_price(self,price):
        self.__holymaxprice = price
c = computerprice()
c.sell()
c.__holymaxprice = 50000
c.set_holy_ultra_pro_max_price(50000)
c.sell()
