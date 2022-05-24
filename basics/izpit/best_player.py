name = input()
goals_scored = int(input())
had_hattrick = False
has_most_goals = False
top_goalscorer = ""
max_goals = 0
while name != "END":
    if goals_scored >= 3:
        had_hattrick = True
    if goals_scored > max_goals:
        max_goals = goals_scored
        has_most_goals = True
        top_goalscorer = name
    if goals_scored >= 10:
        break
    name = input()
    if name == "END":
        break
    goals_scored = int(input())
if has_most_goals:
    print(f"{top_goalscorer} is the best player!")
if had_hattrick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {goals_scored} goals.")


