inventory = {}
command = input()
while command != 'statistics':
    stock = command.split(': ')
    item = stock[0]
    amount = int(stock[1])
    if item not in inventory:
        inventory[item] = 0
    inventory[item] += amount
    command = input()
total_products = len(inventory.keys())
total_quantity = sum(inventory.values())
print('Products in stock:')
for key, value in inventory.items():
    print(f"- {key}: {value}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")