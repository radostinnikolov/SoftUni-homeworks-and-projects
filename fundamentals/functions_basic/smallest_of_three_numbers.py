import sys


def get_smallest(first, second, third):
    list_of_nums = [first, second, third]
    smallest_num = sys.maxsize
    for i in list_of_nums:
        if i < smallest_num:
            smallest_num = i
    return smallest_num


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(get_smallest(first_num, second_num, third_num))


