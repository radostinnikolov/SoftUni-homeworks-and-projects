budget = float(input())
statists_number = int(input())
costume_price = float(input())

decor = 0.1 * budget
costume_total = statists_number * costume_price

if statists_number > 150:
    costume_total *= 0.9

total = costume_total + decor

if total > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(total - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(total - budget):.2f} leva left.")
