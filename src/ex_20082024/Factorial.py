# ✅ Factorial n = 5 5! -->54321 -> 120 3! -> 321 -> 6 4! -> 432*1 -> 24

num = int(input("Enter the number for factorial: "))
fact = 1
if num == 0 or num == 1:
    print("factorial is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(f"factorial is {fact}")

# i|  o\p  | fact
# 1|  1*1     | 1
# 2|  fact=1 * i=2   | 2
# 3|  2*3    |6
# 4|  6*4     |24
# 5| 24*5    |120
