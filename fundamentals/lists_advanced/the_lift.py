waiting_people = int(input())
state_of_lift = [int(el) for el in input().split()]


for wagon in range(len(state_of_lift)):
    while state_of_lift[wagon] < 4:
        if waiting_people == 0:
            break
        state_of_lift[wagon] += 1
        waiting_people -= 1
    if waiting_people == 0 and sum(state_of_lift) // len(state_of_lift) == 4:
        print(*state_of_lift)
        break
    elif waiting_people == 0:
        print("The lift has empty spots!")
        print(*state_of_lift)
        break
else:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(*state_of_lift)

