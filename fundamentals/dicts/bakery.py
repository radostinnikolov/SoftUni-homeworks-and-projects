products = input().split()
result = {products[i]: int(products[i+1]) for i in range(0, len(products), 2)}
print(result)