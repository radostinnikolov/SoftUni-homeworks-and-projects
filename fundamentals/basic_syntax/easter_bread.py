budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
loaf_of_bread = flour_price + eggs_price + milk_price
bread_counter = 0
eggs_counter = 0
while budget >= loaf_of_bread:
    budget -= loaf_of_bread
    bread_counter += 1
    eggs_counter += 3
    if bread_counter % 3 == 0:
        eggs_counter -= bread_counter - 2
print(f"You made {bread_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")


