def order(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.00
    return price * quantity

product = input()
amount = int(input())
print(f"{order(product, amount):.2f}")
