print("Hello World")

print("\n------------- Print Type ------------------")
x = 3.14
print(f"x type: {type(x)}")

# x = int(x) => int type
# x = str(x) => str type
print("\n------------- Array ------------------")
point = [98,99,100]
print(point)
# 追加
point.append(97)
print(f"追加97 : {point}")
# 削除
point.remove(100)
print(f"削除100 : {point}")

print("\n------------- Random ------------------")
import random
kuji = ["大凶","凶","末吉","小吉","中吉","大吉"]
print(f"今日の運勢は{random.choice(kuji)}です")

