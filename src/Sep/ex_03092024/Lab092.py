# Take input and create a class in python

class Person:

    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter your age\n")
        self.phone = input("Enter your phone\n")
        self.occupation = input("Enter your occupation\n")
        self.id = "h12bd"

    def display_details(self):
        # print(self.name)
        # print(self.age)
        # print(self.phone)
        # print(self.occupation)
        # print(self.id)
        print(f"Name is {self.name}", f"Age is {self.age}", f"Phone is {self.phone}",
              f"occupation is {self.occupation}")


# create object
person1 = Person()
# Call the display Function
person1.display_details()
