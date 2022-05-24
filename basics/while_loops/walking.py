goal = 10000
total = 0
reached_goal = False
while reached_goal is False:
    command = input()
    if command == "Going home":
        steps = int(input())
        total += steps
        if total >= goal:
            reached_goal = True
        break
    else:
        command = int(command)
        total += command
    if total >= goal:
        reached_goal = True
diff = abs(total - goal)
if reached_goal is True:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")





