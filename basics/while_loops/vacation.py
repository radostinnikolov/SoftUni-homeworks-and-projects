needed_money = float(input())
money_on_hand = float(input())
total_days = 0
spend_counter = 0
while money_on_hand < needed_money:
    total_days += 1
    action = input()
    sum_of_money = float(input())
    if action == "save":
        money_on_hand += sum_of_money
        spend_counter = 0
    else:
        money_on_hand -= sum_of_money
        spend_counter += 1
        if spend_counter == 5:
            break
        if money_on_hand < 0:
            money_on_hand = 0
if money_on_hand >= needed_money:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(f"{total_days}")