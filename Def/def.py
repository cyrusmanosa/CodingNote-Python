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

print("\n--------------- def (function) 3 -----------------")

def multiply(*numbers):
    total = 1
    for number in numbers: 
        total *= number
    return total
    
print(multiply(2,3,4,5))