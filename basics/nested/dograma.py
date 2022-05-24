number_of_dogramis = int(input())
type_dograma = input()
delivery = input()
price = 0
if type_dograma == "90X130":
    price = 110
    if 30 < number_of_dogramis <= 60:
        price *= 0.95
    elif number_of_dogramis > 60:
        price *= 0.92
elif type_dograma == "100X150":
    price = 140
    if 40 < number_of_dogramis <= 80:
        price *= 0.94
    elif number_of_dogramis > 80:
        price *= 0.9
elif type_dograma == "130X180":
    price = 190
    if 20 < number_of_dogramis <= 50:
        price *= 0.93
    elif number_of_dogramis > 50:
        price *= 0.88
elif type_dograma == "200X300":
    price = 250
    if 25 < number_of_dogramis <= 50:
        price *= 0.91
    elif number_of_dogramis > 50:
        price *= 0.86
total = number_of_dogramis * price
if delivery == "With delivery":
    total += 60
if number_of_dogramis > 100:
    total *= 0.96
    print(f"{total:.2f} BGN")
elif number_of_dogramis <= 10:
    print("Invalid order")
else:
    print(f"{total:.2f} BGN")



