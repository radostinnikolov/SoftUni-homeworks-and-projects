budget = int(input())
season = input()
number_of_fishermen = int(input())
rent = 0

if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

if number_of_fishermen <= 6:
    rent *= 0.9
elif number_of_fishermen <= 11:
    rent *= 0.85
elif number_of_fishermen >= 12:
    rent *= 0.75

total = rent
if number_of_fishermen % 2 == 0 and season != "Autumn":
    total *= 0.95

difference = abs(total - budget)
if total > budget:
    print(f"Not enough money! You need {difference:.2f} leva.")
else:
    print(f"Yes! You have {difference:.2f} leva left.")