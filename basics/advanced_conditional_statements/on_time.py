exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_in_minutes = exam_hour * 60 + exam_minutes
arrival_in_minutes = arrival_hour * 60 + arrival_minutes
hours = abs(arrival_in_minutes - exam_in_minutes) // 60
minutes = abs(arrival_in_minutes - exam_in_minutes) % 60

if arrival_in_minutes > exam_in_minutes:
    print("Late")
elif arrival_in_minutes >= exam_in_minutes - 30:
    print("On time")
elif arrival_in_minutes < exam_in_minutes - 30:
    print("Early")

if exam_in_minutes > arrival_in_minutes > exam_in_minutes - 60:
    print(f"{minutes} minutes before the start")
elif arrival_in_minutes <= exam_in_minutes - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif exam_in_minutes < arrival_in_minutes < exam_in_minutes + 60:
    print(f"{minutes} minutes after the start")
elif arrival_in_minutes >= exam_in_minutes + 60:
    print(f"{hours}:{minutes:02d} hours after the start")