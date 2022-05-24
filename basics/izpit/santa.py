import math

days_missing = int(input())
total_food = int(input())
first_deer_per_day = float(input())
second_deer_per_day = float(input())
third_deer_per_day = float(input())

food_left = total_food - (first_deer_per_day * days_missing + second_deer_per_day * days_missing + third_deer_per_day * days_missing)
if food_left > 0:
    print(f"{math.floor(food_left)} kilos of food left.")
else:
    print(f"{math.ceil(abs(food_left))} more kilos of food are needed.")