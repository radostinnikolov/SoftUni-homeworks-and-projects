fires = input().split("#")
water_amount = int(input())
valid_fires = []
effort = 0
total_fire = 0
fires_put_out = []
for fire in fires:
    current_fire = fire.split(" = ")
    if current_fire[0] == "High":
        if 81 <= int(current_fire[1]) <= 125:
            valid_fires.append(current_fire)
    elif current_fire[0] == "Medium":
        if 51 <= int(current_fire[1]) <= 80:
            valid_fires.append(current_fire)
    elif current_fire[0] == "Low":
        if 1 <= int(current_fire[1]) <= 50:
            valid_fires.append(current_fire)
while water_amount > 0:
    for fire in valid_fires:
        if water_amount <= 0:
            break
        if water_amount < int(fire[1]):
            continue
        water_amount -= int(fire[1])
        effort += 0.25 * int(fire[1])
        total_fire += int(fire[1])
        fires_put_out.append(int(fire[1]))
    break

print("Cells:")
for fire_value in fires_put_out:
    print(f" - {fire_value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

