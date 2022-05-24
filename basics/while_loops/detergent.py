bottles_of_detergent = int(input())
available_detergent = bottles_of_detergent * 750
detergent_is_over = False
plate = 5
pot = 15
counter_total = 0
counter_plates = 0
counter_pots = 0
user_input = input()
while user_input != "End":
    counter_total += 1
    if counter_total % 3 == 0:
        available_detergent -= int(user_input) * pot
        counter_pots += int(user_input)
    else:
        available_detergent -= int(user_input) * plate
        counter_plates += int(user_input)
    if available_detergent < 0:
        detergent_is_over = True
        break
    user_input = input()
if detergent_is_over is True:
    print(f"Not enough detergent, {abs(available_detergent)} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{counter_plates} dishes and {counter_pots} pots were washed.")
    print(f"Leftover detergent {available_detergent} ml.")