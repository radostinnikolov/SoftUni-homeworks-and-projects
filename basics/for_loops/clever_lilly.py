age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toy_amount = 0
money = 0
money_per_even = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        money_per_even += 10
        money += money_per_even - 1
    else:
        toy_amount += 1
total = money + toy_amount * toy_price
diff = abs(total - washing_machine_price)
if total >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

