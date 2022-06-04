user_input = input().split(" ")
nums_to_remove = int(input())

list_of_ints = [int(i) for i in user_input]
list_copy = list_of_ints.copy()
smallest_nums = []
list_copy.sort()
for i in range(nums_to_remove):
    smallest_nums.append(list_copy.pop(0))

while smallest_nums:
    for num in list_of_ints:
        if num in smallest_nums:
            list_of_ints.remove(num)
            smallest_nums.remove(num)

for i in range(len(list_of_ints)):
    if i == len(list_of_ints) - 1:
        print(list_of_ints[i], end="")
    else:
        print(list_of_ints[i],  end=", ")
