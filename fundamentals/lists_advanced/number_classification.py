numbers_pool = [int(el) for el in input().split(", ")]
print(f"Positive: {', '.join([str(num) for num in numbers_pool if num >= 0])}")
print(f"Negative: {', '.join([str(num) for num in numbers_pool if num < 0])}")
print(f"Even: {', '.join([str(num) for num in numbers_pool if num % 2 == 0])}")
print(f"Odd: {', '.join([str(num) for num in numbers_pool if num % 2 != 0])}")
