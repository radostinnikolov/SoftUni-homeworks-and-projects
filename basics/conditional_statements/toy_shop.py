puzzle_price = 2.6
doll_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2

price_holiday = float(input())
puzzle_amount = int(input())
doll_amount = int(input())
bear_amount = int(input())
minion_amount = int(input())
truck_amount = int(input())
total_amount = puzzle_amount + doll_amount + bear_amount + minion_amount + truck_amount

total = puzzle_amount * puzzle_price \
    + doll_amount * doll_price \
    + bear_amount * bear_price \
    + minion_amount * minion_price \
    + truck_price * truck_amount

if total_amount >= 50:
    total = total * 0.75

total = total * 0.9

if total >= price_holiday:
    print(f"Yes! {total - price_holiday:.2f} lv left.")
else:
    print(f"Not enough money! {abs(total - price_holiday):.2f} lv needed.")
