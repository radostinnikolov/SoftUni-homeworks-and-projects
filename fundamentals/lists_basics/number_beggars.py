numbers = input().split(", ")
number_of_beggars = int(input())
numbers_as_ints = [int(i) for i in numbers]
final_list = []
beggar = 0
curr_sum = 0
while beggar < number_of_beggars:
    for i in range(beggar, len(numbers_as_ints), number_of_beggars):
        curr_sum += numbers_as_ints[i]
    final_list.append(curr_sum)
    beggar += 1
    curr_sum = 0
print(final_list)


