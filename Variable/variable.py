import math

name = "ECC"
age = 20
first = "Cyrus"
last = "Man"
full = f"{first} {last}"
print(age)
print(full.find("Ma"))
print("us" in full)
print("usxxx" not in full)
print(f"名前：{name}年齢：{age}")

# 整數
print(round(2.9))

# 正數
print(abs(-2.1))

# 小數進正數
print(math.ceil(2.2))

# input == scanner  
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

# -1 ==> 最大
ff = "Apple"
print(ff[1:-1])

# 計開首的字母char 
print("bag">"cppsadasdlse")