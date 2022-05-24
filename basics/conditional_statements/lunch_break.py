import math

name = input()
episode_length = int(input())
break_time = int(input())

lunch_time = 1/8 * break_time
relax_time = 1/4 * break_time

condition = (break_time - (lunch_time + relax_time)) >= episode_length
time_left = abs((break_time - (lunch_time + relax_time) - episode_length))
if condition:
    print(f"You have enough time to watch {name} and left with {math.ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(time_left)} more minutes.")
