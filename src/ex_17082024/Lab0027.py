# Create a program that takes two numbers as input and prints whether the first number is
# greater than, less than, or equal to the second number.

n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))

if n1 > n2:
    print("first number is greater than other number")
elif n1 < n2:
    print("first number is less than other number")
else:
    print("first number is equal to other number")
