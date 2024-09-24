print("\n--------------- def (function) 1 -----------------")

def postTaxPrice1(price):
    ans = int(price * 1.1)
    return ans

print(postTaxPrice1(100))

print("\n--------------- def (function) 2 -----------------")

def postTaxPrice2(price,name):
    ans = int(price * 1.1)
    return ans

print(postTaxPrice2(name="apple",price=100))