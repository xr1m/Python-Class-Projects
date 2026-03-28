# Is this a bus:

class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    pass

result = bus("School Bus", 130, 15)
print(f"The name of the bus is: {result.name}\nThe max speed is: {result.maxspeed}\nand the mileage is: {result.mileage}")