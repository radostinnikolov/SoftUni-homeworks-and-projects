all_numbers = [int(el) for el in input().split(", ")]
limit = 10
all_groups = []
while all_numbers:
    current_group = []
    for num in all_numbers:
        if num <= limit:
            current_group.append(num)
    limit += 10
    all_groups.append(current_group)
    for i in current_group:
        all_numbers.remove(i)
group_number = 10
for group in all_groups:
    print(f"Group of {group_number}'s: {group}")
    group_number += 10
