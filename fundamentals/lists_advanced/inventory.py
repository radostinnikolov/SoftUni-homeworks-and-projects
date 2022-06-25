def collect(item, journal):
    if item not in journal:
        journal.append(item)
    return


def drop(item, journal):
    if item in journal:
        journal.remove(item)
    return


def combine(old_item, new_item, journal):
    if old_item in journal:
        old_item_index = journal.index(old_item)
        new_item_index = old_item_index + 1
        if new_item_index > len(journal) - 1:
            journal.append(new_item)
        else:
            journal.insert(new_item_index, new_item)
    return


def renew(item, journal):
    if item in journal:
        item_index = journal.index(item)
        journal.append(journal.pop(item_index))
    return


journal = input().split(", ")
command = input()
while command != "Craft!":
    current_command = command.split(" - ")
    order = current_command[0]
    if order == "Collect":
        current_item = current_command[1]
        collect(current_item, journal)
    elif order == "Drop":
        current_item = current_command[1]
        drop(current_item, journal)
    elif order == "Combine Items":
        items_for_combine = current_command[1].split(":")
        old_item = items_for_combine[0]
        new_item = items_for_combine[1]
        combine(old_item, new_item, journal)
    elif order == "Renew":
        current_item = current_command[1]
        renew(current_item, journal)
    command = input()
print(*journal, sep=", ")


