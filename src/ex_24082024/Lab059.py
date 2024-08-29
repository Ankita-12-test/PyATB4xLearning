# Create a program to sum of three number from the user input
# using functions

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


def sum_of_three_num(num1, num2, num3):
    return num1 + num2 + num3


a = sum_of_three_num(num1, num2, num3)
print(f"sum of three numbers is {a}")
