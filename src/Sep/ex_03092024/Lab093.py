class Calc():

    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b


Calc1 = Calc()
a = float(input("Enter the no1"))
b = float(input("Enter the no2"))

multiply = Calc1.mul(a, b)
Add = Calc1.sum(a, b)
Subt = Calc1.sub(a, b)
print(multiply, Add, Subt)
