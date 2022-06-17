first_input = input().split(", ")
second_input = input().split(", ")
result = []
for first in first_input:
    for second in second_input:
        if first in second:
            result.append(first)
            break
print(result)