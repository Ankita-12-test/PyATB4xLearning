import math
try:
    a = int(input("Enter the num to get exponential of:"))
    result = math.exp(a)
    print("Exponential is", result)
except Exception as e:
    print(e)
    print("Kindly enter low values")