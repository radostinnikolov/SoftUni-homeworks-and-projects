def increase_or_decrease(sequence, item):
    for i in range(len(sequence)):
        if sequence[i] <= item:
            sequence[i] += item
        elif sequence[i] > item:
            sequence[i] -= item
    return item


def index_less_than_zero(sequence):
    current_item = sequence.pop(0)
    sequence.insert(0, sequence[-1])
    return current_item

def index_more_than_last_index(sequence):
    current_item = sequence.pop(-1)
    sequence.append(sequence[0])
    return current_item




seq_of_integers = [int(el) for el in input().split()]
sum_for_output = 0
while seq_of_integers:
    current_index = int(input())
    if current_index < 0:
        sum_for_output += increase_or_decrease(seq_of_integers, index_less_than_zero(seq_of_integers))
    elif current_index > len(seq_of_integers) - 1:
        sum_for_output += increase_or_decrease(seq_of_integers, index_more_than_last_index(seq_of_integers))
    else:
        current_item = seq_of_integers.pop(current_index)
        sum_for_output += increase_or_decrease(seq_of_integers, current_item)
print(sum_for_output)
