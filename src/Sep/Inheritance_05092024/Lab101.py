a = 10 #global variable

class Myclass:

    public_var = "Im public in nature"
    balance = 100
    c = 10
    _b= 11
    __d = 12

    __private_var = "Im private in nature due to __ this symbol"
    __password = 1123

    _protected_var = "Im protected in nature due to _ this symbol"

object = Myclass()
print(object.public_var)
print(object._protected_var)
print(object.balance)
print(object._b)
