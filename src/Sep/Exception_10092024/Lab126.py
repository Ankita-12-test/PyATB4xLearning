# try :
#     # Try this code , if error
# except:
#     # Excute me if try has some error


print("------------START PROGRAM------------")
try:
    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    c = a/b
    print("Divsion of thr no is", c)
except Exception as e:# alias , Exception is what Class - multiple classes
    print(e)
    print("Please check your inputs, it shouldn't be a string or zero")
print("------------STOP PROGRAM------------")