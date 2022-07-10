products = input().split()
bakery = {products[i]: int(products[i+1]) for i in range(0, len(products), 2)}
wanted_products = input().split()
for item in wanted_products:
    if item not in bakery:
        print(f"Sorry, we don't have {item}")
    else:
        print(f"We have {bakery[item]} of {item} left")