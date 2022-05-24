a = int(input())
b = int(input())
max_amount = int(input())
i = 35
j = 64
counter = 0
result = ""
for k in range(1, a + 1):
    third = str(k)
    for m in range(1, b + 1):
        fourth = str(m)
        while i >= 35:
            first = chr(i)
            i += 1
            if i > 55:
                i = 35
            break
        while j >= 64:
            second = chr(j)
            j += 1
            if j > 96:
                j = 64
            break
        result = first + second + third + fourth + second + first
        print(result, end="|")
        counter += 1
        if counter >= max_amount:
            break
    if counter >= max_amount:
        break

