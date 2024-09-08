"""Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}"""

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
print(f"{max(num1, num2)} is maximum number")
print(f"{pow(num1, num2)}power of num1 to num2 is")
print(f"{num1 - num2} sub of num is")
print(f"{num1 + num2} add of num is")
print(f"{num1 * num2} mul of num is")
print(f"{num1 / num2} div of num is")
