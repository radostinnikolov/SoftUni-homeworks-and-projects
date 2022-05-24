number_of_dancers = int(input())
points = float(input())
season = input()
place = input()
money_won = 0
if place == "Bulgaria":
    money_won = points * number_of_dancers
    if season == "summer":
        money_won *= 0.95
    else:
        money_won *= 0.92
else:
    money_won = (points * number_of_dancers) + 0.5 * (points * number_of_dancers)
    if season == "summer":
        money_won *= 0.9
    else:
        money_won *= 0.85
charity = money_won * 0.75
money_left = money_won - charity
money_per_dancer = money_left / number_of_dancers
print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
