budget = float(input())
season = input()
destination = ""
money_needed = 0
type_of_vacation = ""


if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        type_of_vacation = "Camp"
        money_needed = 0.3 * budget
    elif season == "winter":
        type_of_vacation = "Hotel"
        money_needed = 0.7 * budget
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        type_of_vacation = "Camp"
        money_needed = 0.4 * budget
    elif season == "winter":
        type_of_vacation = "Hotel"
        money_needed = 0.8 * budget
elif budget > 1000:
    destination = "Europe"
    money_needed = 0.9 * budget
    type_of_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {money_needed:.2f}")



