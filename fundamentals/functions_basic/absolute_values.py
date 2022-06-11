def abs_nums(some_numbers):
    absol_nums = []
    for i in some_numbers:
        absol_nums.append(abs(i))
    return absol_nums


numbers = [float(el) for el in input().split()]

print(abs_nums(numbers))
