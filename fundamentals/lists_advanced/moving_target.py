def shoot(index, power, targets):
    if 0 <= index <= len(targets) - 1:
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)


def add(index, value, targets):
    if 0 <= index <= len(targets) - 1:
        targets.insert(index, value)
    else:
        print("Invalid placement!")


def strike(index, radius, targets):
    range_for_strike = targets[index - radius:index + radius + 1]
    if len(range_for_strike) == 2*radius + 1:
        del targets[index - radius:index + radius + 1]
    else:
        print("Strike missed!")


targets = [int(el) for el in input().split()]
command = input()
while command != "End":
    current_command = command.split()
    order = current_command[0]
    if order == "Shoot":
        index = int(current_command[1])
        power = int(current_command[2])
        shoot(index, power, targets)
    elif order == "Add":
        index = int(current_command[1])
        value = int(current_command[2])
        add(index, value, targets)
    elif order == "Strike":
        index = int(current_command[1])
        radius = int(current_command[2])
        strike(index, radius, targets)
    command = input()
print(*targets, sep="|")

