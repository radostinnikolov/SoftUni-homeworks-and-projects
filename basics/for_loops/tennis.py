import math

number_of_tournaments = int(input())
starting_points = int(input())
total_points = 0
avg_points = 0
points_from_tournaments = 0
wins = 0
for i in range(number_of_tournaments):
    result = input()
    if result == "W":
        points_from_tournaments += 2000
        wins += 1
    elif result == "F":
        points_from_tournaments += 1200
    elif result == "SF":
        points_from_tournaments += 720
avg_points = points_from_tournaments / number_of_tournaments
total_points = points_from_tournaments + starting_points
percent_wins = wins / number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(avg_points)}")
print(f"{percent_wins:.2f}%")




