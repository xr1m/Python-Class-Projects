# Computer Price:

class Computer():
    def __init__(self):
        self.__maxprice = 900
    def sellingprice(self):
        print(f"Selling Price: {self.__maxprice}")
    def maxprice(self, price):
        self.__maxprice = price

ob = Computer()
ob.sellingprice()
ob.__maxprice = 1000
ob.sellingprice()
ob.maxprice(1000)
ob.sellingprice()