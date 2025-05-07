print("--------------- if -----------------")

x = 1
if x <= 1:
    print("xは1以下です")
else:
    print("xは1以上です")

y = 22
if y >= 10 and y <= 20:
    print("yは10から20の間です")
elif y < 10:
    print("yは10未満です")

print("Done!")

age = 12
msg = "Eligible" if age >= 18 else "Not Eligible"
print(msg)

if 790 > age >= 6:
    print("Yes")


abcd = "asdasdasd"
if not abcd:
    print("abcdは空です")
