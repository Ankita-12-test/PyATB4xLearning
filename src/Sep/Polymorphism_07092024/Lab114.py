# Method overriding
# says that, Child or subclass can have same name method as the parent or super class

class Shape:
    def area(self):
        print("Print the AREA of the shape")

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width  = width
    def area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # def area(self):
    #     return 3.14 * self.radius * self.radius

r = Rectangle(3,4)
print(r.area())

c = Circle(4)
print(c.area())

