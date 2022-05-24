day = input()

workday = day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"
weekend = day == "Saturday" or day == "Sunday"

if workday:
    print("Working day")
elif weekend:
    print("Weekend")
else:
    print("Error")
