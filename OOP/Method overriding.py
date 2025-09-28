# prent class to redifind in child class
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x*self.y


class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius


rec = Shape(3, 5)
print(rec.area())
c = circle(5)