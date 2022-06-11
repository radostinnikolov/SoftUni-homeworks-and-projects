def min_max_sum(some_numbers):
    min_num = min(some_numbers)
    max_num = max(some_numbers)
    sum_nums = sum(some_numbers)
    return f"The minimum number is {min_num}\n" \
           f"The maximum number is {max_num}\n" \
           f"The sum number is: {sum_nums}"




numbers = [int(el) for el in input().split()]
print(min_max_sum(numbers))
