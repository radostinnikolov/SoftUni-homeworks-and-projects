type_flower = input()
amount = int(input())
budget = int(input())
price = 0

if type_flower == "Roses":
    price = 5
    if amount > 80:
        price *= 0.9
elif type_flower == "Dahlias":
    price = 3.8
    if amount > 90:
        price *= 0.85
elif type_flower == "Tulips":
    price = 2.8
    if amount > 80:
        price *= 0.85
elif type_flower == "Narcissus":
    price = 3
    if amount < 120:
        price *= 1.15
elif type_flower == "Gladiolus":
    price = 2.5
    if amount < 80:
        price *= 1.2
total = amount * price
difference = abs(total - budget)

if total > budget:
    print(f"Not enough money, you need {difference:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {amount} {type_flower} and {difference:.2f} leva left.")