def merge(str_list, start, end):
    start = int(start)
    end = int(end)
    if end > len(str_list) - 1:
        end = len(str_list) - 1
    if end < 0:
        end = 0
    if start > len(str_list) - 1:
        start = len(str_list) - 1
    if start < 0:
        start = 0
    resulting_string = ""
    for i in range(start, end + 1):
        resulting_string += str_list[i]
    str_list[start:end] = ""
    str_list[start] = resulting_string
    return


def divide(str_list, index, partitions):
    index = int(index)
    partitions = int(partitions)
    if partitions == 0:
        return
    current_string = str_list.pop(index)
    length_of_substring = len(current_string) // partitions
    index_for_insert = index
    if len(current_string) % partitions == 0:
        for i in range(partitions):
            substring = current_string[:length_of_substring]
            str_list.insert(index_for_insert, substring)
            current_string = current_string[length_of_substring:]
            index_for_insert += 1
    else:
        for i in range(partitions - 1):
            substring = current_string[:length_of_substring]
            str_list.insert(index_for_insert, substring)
            current_string = current_string[length_of_substring:]
            index_for_insert += 1
        str_list.insert(index_for_insert, current_string)
    return


strings_list = [element for element in input().split()]
command = input()
while command != "3:1":
    command_list = command.split()
    order = command_list[0]
    if order == "merge":
        start_index = command_list[1]
        end_index = command_list[2]
        merge(strings_list, start_index, end_index)
    elif order == "divide":
        index = command_list[1]
        partitions = command_list[2]
        divide(strings_list, index, partitions)
    command = input()
print(*strings_list)