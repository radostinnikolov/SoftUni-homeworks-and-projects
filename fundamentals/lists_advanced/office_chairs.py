number_of_rooms = int(input())
total_free_chairs = 0
total_chairs = 0
total_visitors = 0
for room in range(1, number_of_rooms + 1):
    data = input().split()
    available_chairs = len(data[0])
    visitors = int(data[1])
    total_chairs += available_chairs
    total_visitors += visitors
    difference = available_chairs - visitors
    if available_chairs >= visitors:
        total_free_chairs += difference
    elif available_chairs < visitors:
        print(f"{abs(difference)} more chairs needed in room {room}")
if total_chairs >= total_visitors:
    print(f"Game On, {total_free_chairs} free chairs left")
