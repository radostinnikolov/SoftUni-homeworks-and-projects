number_of_balls = int(input())
points = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
black_counter = 0
not_accepted_ball = 0

for i in range (number_of_balls):
    color = input()
    if color == "red":
        red_counter += 1
        points += 5
    elif color == "orange":
        orange_counter += 1
        points += 10
    elif color == "yellow":
        yellow_counter += 1
        points += 15
    elif color == "white":
        white_counter += 1
        points += 20
    elif color == "black":
        black_counter += 1
        points //= 2
    else:
        not_accepted_ball += 1
print(f"Total points: {points}")
print(f"Red balls: {red_counter}")
print(f"Orange balls: {orange_counter}")
print(f"Yellow balls: {yellow_counter}")
print(f"White balls: {white_counter}")
print(f"Other colors picked: {not_accepted_ball}")
print(f"Divides from black balls: {black_counter}")