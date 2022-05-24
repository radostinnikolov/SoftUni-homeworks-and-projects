name_actor = input()
academy_points = float(input())
number_of_judges = int(input())
total_points = 0
total_points += academy_points

for i in range(number_of_judges):
    if total_points > 1250.5:
        break
    name_judge = input()
    points_judge = float(input())
    points_given = (len(name_judge) * points_judge) / 2
    total_points += points_given

if total_points > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
