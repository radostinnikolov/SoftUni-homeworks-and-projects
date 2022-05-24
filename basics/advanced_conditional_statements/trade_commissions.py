city = input()
sales = float(input())
commission = 0


cities = {"Sofia", "Varna", "Plovdiv"}
condition0 = city not in cities
condition1 = sales < 0
condition2 = 0 <= sales <= 500
condition3 = sales <= 1000
condition4 = sales <= 10000
condition5 = sales > 10000

if condition2:
    if city == "Sofia":
        commission = sales * 0.05
    elif city == "Varna":
        commission = sales * 0.045
    elif city == "Plovdiv":
        commission = sales * 0.055
elif condition3:
    if city == "Sofia":
        commission = sales * 0.07
    elif city == "Varna":
        commission = sales * 0.075
    elif city == "Plovdiv":
        commission = sales * 0.08
elif condition4:
    if city == "Sofia":
        commission = sales * 0.08
    elif city == "Varna":
        commission = sales * 0.1
    elif city == "Plovdiv":
        commission = sales * 0.12
elif condition5:
    if city == "Sofia":
        commission = sales * 0.12
    elif city == "Varna":
        commission = sales * 0.13
    elif city == "Plovdiv":
        commission = sales * 0.145
if condition0 or condition1:
    print("error")
else:
    print(f"{commission:.2f}")

