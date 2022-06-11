def round_nums(some_numbers):
    rounded_nums = []
    for i in some_numbers:
        rounded_nums.append(round(i))
    return rounded_nums


nums = [float(el) for el in input().split()]
print(round_nums(nums))
