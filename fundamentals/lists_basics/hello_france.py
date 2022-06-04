target = 150
collection_of_items = input().split("|")
budget = float(input())
profit = 0
valid_items = []

for item in collection_of_items:
    current_item = item.split("->")
    item_name = current_item[0]
    item_price = float(current_item[1])
    if item_name == "Clothes":
        if item_price <= 50:
            if budget >= item_price:
                budget -= item_price
                valid_items.append(current_item)
    elif item_name == "Shoes":
        if item_price <= 35:
            if budget >= item_price:
                budget -= item_price
                valid_items.append(current_item)
    elif item_name == "Accessories":
        if item_price <= 20.50:
            if budget >= item_price:
                budget -= item_price
                valid_items.append(current_item)

prices_before_sell = [float(item[1]) for item in valid_items]
valid_items_price_markup = [float(item[1]) * 1.4 for item in valid_items]
for index in range(len(valid_items_price_markup)):
    profit += valid_items_price_markup[index] - prices_before_sell[index]

budget_after_selling = sum(valid_items_price_markup) + budget

for price in valid_items_price_markup:
    print(f"{price:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if budget_after_selling >= target:
    print("Hello, France!")
else:
    print("Not enough money.")
