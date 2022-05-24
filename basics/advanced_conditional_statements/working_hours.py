hour = int(input())
day = input()

working_hours = {10, 11, 12, 13, 14, 15, 16, 17, 18}
working_days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}

if hour in working_hours and day in working_days:
    print("open")
else:
    print("closed")