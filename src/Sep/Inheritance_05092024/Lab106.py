class Son:
    gold = "1kg"

class Father(Son):
    diamond = "22karat"

class GrandFather(Father):
    btc = "1btc"

g = GrandFather()
print(g.diamond)
print(g.gold)