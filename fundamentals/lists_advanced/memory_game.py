def check_for_valid_index(index1, index2, moves, sequence):
    if index1 == index2 or (len(sequence) - 1) < index1 or index1 < 0 or (len(sequence) - 1) < index2 or index2 < 0:
        place_for_insert = len(sequence) // 2
        sequence.insert(place_for_insert, f"-{moves}a")
        sequence.insert(place_for_insert, f"-{moves}a")
        return False
    else:
        return True


def check_elements(index1, index2, sequence):
    if sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        item2 = sequence[index2]
        item1 = sequence[index1]
        sequence.remove(item2)
        sequence.remove(item1)
    else:
        print("Try again!")


def check_if_won(sequence, moves):
    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        return True


all_nums = input().split()
current_moves = 0
command = input()
while command != "end":
    current_moves += 1

    current_command = command.split()
    first_index = int(current_command[0])
    second_index = int(current_command[1])
    if check_for_valid_index(first_index, second_index,current_moves,all_nums):
        check_elements(first_index, second_index, all_nums)
        if check_if_won(all_nums, current_moves):
            break
    else:
        print("Invalid input! Adding additional elements to the board")

    command = input()
else:
    if len(all_nums) > 0:
        print(f"Sorry you lose :(")
        print(*all_nums)