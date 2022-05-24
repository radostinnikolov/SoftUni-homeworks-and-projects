amount = int(input())
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
for i in range(amount):
    current_num = int(input())
    if current_num < 200:
        sum1 += 1
    elif current_num < 400:
        sum2 += 1
    elif current_num < 600:
        sum3 += 1
    elif current_num < 800:
        sum4 += 1
    elif current_num >= 800:
        sum5 += 1
p1 = sum1 / amount * 100
p2 = sum2 / amount * 100
p3 = sum3 / amount * 100
p4 = sum4 / amount * 100
p5 = sum5 / amount * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

