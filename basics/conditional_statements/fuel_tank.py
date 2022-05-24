type_of_fuel = input()
amount_left = float(input())

if amount_left >= 25 and type_of_fuel in {"Gas", "Gasoline", "Diesel"}:
    print(f"You have enough {type_of_fuel.lower()}.")
elif amount_left < 25 and type_of_fuel in {"Gas", "Gasoline", "Diesel"}:
    print(f"Fill your tank with {type_of_fuel.lower()}!")
else:
    print("Invalid fuel!")
