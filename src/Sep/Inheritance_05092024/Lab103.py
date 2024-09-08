# Single inheritance

class Father:
    key = "2BHK"

    def car(self):
        print("Dad has ALTO")

class Son(Father):
    key2 = "3BHK"

    def vehicle(self):
        print("Son has truck")

father_obj = Father()
father_obj.car()
print(father_obj.key)
# ing=heritance comes into the picture
son_obj = Son()
son_obj.vehicle()
son_obj.car()
print(son_obj.key2)
print(son_obj.key)
