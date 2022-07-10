products = {}
command = input()
while command != 'buy':
    input_for_work = command.split()
    name = input_for_work[0]
    price = float(input_for_work[1])
    quantity = int(input_for_work[2])
    if name not in products:
        products[name] = {'price': price, 'quantity': quantity}
    else:
        products[name]['price'] = price
        products[name]['quantity'] += quantity
    command = input()

for key, value in products.items():
    total = value['price'] * value['quantity']
    print(f"{key} -> {total:.2f}")
