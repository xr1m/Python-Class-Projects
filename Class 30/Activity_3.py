# Point Function:

class Point():
    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
ob = Point(10, 12)
print(ob)