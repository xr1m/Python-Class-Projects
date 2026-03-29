# Keep It Private!:

class Private():
    __private = 1000
    def __priv(self):
        print("I am in a class Private")
    def normal(self):
        print("Private Variable value =", Private.__private)

obj1 = Private()
obj1.normal()
obj1.__priv