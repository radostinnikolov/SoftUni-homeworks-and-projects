def sum_numbers(a, b):
    return a + b


def subtract(sum, num):
    return sum - num


def add_and_subtract(first, second, third):
    sum = sum_numbers(first, second)
    result = subtract(sum, third)
    return result

first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))
