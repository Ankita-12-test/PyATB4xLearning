# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

T1 = int(input("Enter the side1: "))
T2 = int(input("Enter the side2: "))
T3 = int(input("Enter the side3: "))

if T1==T2==T3:
    print("triangle is equilateral")
elif T1==T2 or T1==T3 or T2==T3:
    print("triangle is isosceles")
else:
    print("triangle is scalene")