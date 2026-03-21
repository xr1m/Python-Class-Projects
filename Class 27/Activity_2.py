# Class Vehicle:

class Vehicle:
    car = "Audi"
    def __init__(self, mileage, max_speed):
        self.mileage = mileage
        self.max_speed = max_speed
object1 = Vehicle(20, 230)
print(f"Mileage: {object1.mileage}\nMax Speed: {object1.max_speed}")
print(f"Car: {object1.car}")