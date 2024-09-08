# functions with argument, parameters

def greet():
    print("Hello, there!!")


def greet_by_name(pramod): # name -> variable name, argument | parameter
    print("Hello,", pramod)

greet_by_name("Pramod")
greet_by_name(123)
greet_by_name(True)
greet_by_name(3.14)

name = input("Enter ur name: ")
def update_by_name(name):
    print("Hello ", name)

update_by_name(name)