def loot(list_of_items, treasure_chest):
    for item in list_of_items:
        if item not in treasure_chest:
            treasure_chest.insert(0, item)
    return


def drop(index, treasure_chest):
    if -len(treasure_chest) <= index <= len(treasure_chest) - 1:
        treasure_chest.append(treasure_chest.pop(index))
    return


def steal(count_of_items, treasure_chest):
    stolen_items = []
    for i in range(count_of_items):
        if len(treasure_chest) == 0:
            return print(*stolen_items, sep=", ")
        stolen_items.insert(0, treasure_chest.pop())
    return print(*stolen_items, sep=", ")


def calculate_gain(treasure_chest):
    total_length = 0
    chest_is_full = True
    if len(treasure_chest) == 0:
        chest_is_full = False
    else:
        for item in treasure_chest:
            total_length += len(item)
    if chest_is_full:
        result = total_length / len(treasure_chest)
        return print(f"Average treasure gain: {result:.2f} pirate credits.")
    else:
        return print("Failed treasure hunt.")


chest = input().split("|")
command = input()
while command != "Yohoho!":
    current_command = command.split()
    order = current_command[0]
    if order == "Loot":
        looted_items = current_command[1:]
        loot(looted_items, chest)
    elif order == "Drop":
        index = int(current_command[1])
        drop(index, chest)
    elif order == "Steal":
        count = int(current_command[1])
        steal(count, chest)
    command = input()
calculate_gain(chest)


