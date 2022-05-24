days_to_stay = int(input())
type_of_room = input()
mark = input()

nights = days_to_stay - 1
price_one_room = 18
price_apartment = 25
price_president = 35
total = 0

if type_of_room == "room for one person":
    total = price_one_room * nights
elif type_of_room == "apartment":
    total = price_apartment * nights
    if days_to_stay < 10:
        total *= 0.7
    elif 10 <= days_to_stay <= 15:
        total *= 0.65
    else:
        total *= 0.5
elif type_of_room == "president apartment":
    total = price_president * nights
    if days_to_stay < 10:
        total *= 0.9
    elif 10 <= days_to_stay <= 15:
        total *= 0.85
    else:
        total *= 0.8
if mark == "positive":
    total *= 1.25
else:
    total *= 0.9

print(f"{total:.2f}")
