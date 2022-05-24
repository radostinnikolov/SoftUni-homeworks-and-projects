first_number = int(input())
second_number = int(input())
first_range = ord("a")
second_range = ord("a") + second_number
result = ""
for first in range(1, first_number + 1):
    result += str(first)
    for second in range(1, first_number + 1):
        result += str(second)
        for third in range(first_range, second_range):
            result += chr(third)
            for fourth in range(first_range, second_range):
                result += chr(fourth)
                for fifth in range(1, first_number + 1):
                    if fifth > first and fifth > second:
                        result += str(fifth)
                        print(result, end=" ")
                        result = str(first) + str(second) + chr(third) + chr(fourth)
                    else:
                        continue
                result = str(first) + str(second) + chr(third)
                continue
            result = str(first) + str(second)
            continue
        result = str(first)
        continue
    result = ""
    continue







