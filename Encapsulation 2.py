class Computer:

    def __init__(self):
        self.__maxprice = 1000000000000000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000000000000000
c.sell()

c.setMaxPrice(1000000000000000)
c.sell()