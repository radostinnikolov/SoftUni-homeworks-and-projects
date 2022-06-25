def shoot(index, list_of_targets):
    if 0 <= index <= len(list_of_targets) - 1 and list_of_targets[index] != -1:
        for i in range(len(list_of_targets)):
            if list_of_targets[i] != -1:
                if list_of_targets[i] > list_of_targets[index]:
                    list_of_targets[i] -= list_of_targets[index]
                elif list_of_targets[i] <= list_of_targets[index] and i != index:
                    list_of_targets[i] += list_of_targets[index]
        list_of_targets[index] = -1
        return True


targets = [int(el) for el in input().split()]
command = input()
shot_targets_counter = 0
while command != "End":
    current_index = int(command)
    if shoot(current_index, targets):
        shot_targets_counter += 1
    command = input()

string_for_print = ""
for el in targets:
    string_for_print += str(el) + " "

print(f"Shot targets: {shot_targets_counter} -> {string_for_print}")