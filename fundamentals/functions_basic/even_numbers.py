numbers = [int(el) for el in input().split()]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)