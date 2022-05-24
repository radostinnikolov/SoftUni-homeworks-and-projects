number_of_days = int(input())
liters = 0
degrees = 0
for day in range(number_of_days):
    current_liters = float(input())
    current_degrees = float(input())
    liters += current_liters
    degrees += current_degrees * current_liters
avg_degrees = degrees / liters
print(f"Liter: {liters:.2f}")
print(f"Degrees: {avg_degrees:.2f}")
if avg_degrees < 38:
    print("Not good, you should baking!")
elif avg_degrees <= 42:
    print("Super!")
else:
    print("Dilution with distilled water!")
