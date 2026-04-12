# Overload Operators:

class operator:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if self.a < other.a:
            return "Object 1 is lesser than object 2"
        else:
            return "Object 1 is more than object 2"
    def __eq__(self, other):
        if self.a == other.a:
            return "Object 1 is equal to object 2"
        else:
            return "Object 1 is not equal to object 2"

obj1 = operator(5)
obj2 = operator(10)
obj3 = operator(9)
obj4 = operator(9)
print(f"Pass value = {obj1.a}, {obj2.a}")
print(obj1 < obj2)

print(f"Pass value = {obj3.a}, {obj4.a}")
print(obj3 == obj4)