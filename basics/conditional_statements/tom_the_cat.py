rest_days = int(input())
limit_for_play_mins = 30000
play_when_working_mins = 63
play_when_resting_mins = 127
playtime_in_workday = (365 - rest_days) * play_when_working_mins
playtime_in_restday = rest_days * play_when_resting_mins
playtime_total = playtime_in_restday + playtime_in_workday

if limit_for_play_mins > playtime_total:
    remaining_time = limit_for_play_mins - playtime_total
    print(f"Tom sleeps well")
    print(f"{remaining_time // 60} hours and {remaining_time % 60} minutes less for play")
elif limit_for_play_mins < playtime_total:
    remaining_time = abs(limit_for_play_mins - playtime_total)
    print(f"Tom will run away")
    print(f"{remaining_time // 60} hours and {remaining_time % 60} minutes more for play")


