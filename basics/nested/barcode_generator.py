start = int(input())
end = int(input())
first_start = start // 1000
second_start = (start % 1000) // 100
third_start = ((start % 1000) % 100) // 10
fourth_start = ((start % 1000) % 100) % 10
first_end = end // 1000
second_end = (end % 1000) // 100
third_end = ((end % 1000) % 100) // 10
fourth_end = ((end % 1000) % 100) % 10
result = ""
for i in range(start, end + 1):
    result = ""
    first_number = i // 1000
    second_number = i % 1000 // 100
    third_number = i % 1000 % 100 // 10
    fourth_number = i % 1000 % 100 % 10
    if first_number in range(first_start, first_end + 1):
        if first_number % 2 != 0:
            result += str(first_number)
        else:
            continue
        if second_number in range(second_start, second_end + 1):
            if second_number % 2 != 0:
                result += str(second_number)
            else:
                continue
            if third_number in range(third_start, third_end + 1):
                if third_number % 2 != 0:
                    result += str(third_number)
                else:
                    continue
                if fourth_number in range(fourth_start, fourth_end + 1):
                    if fourth_number % 2 != 0:
                        result += str(fourth_number)
                        print(result + " ", end="")
                        result = ""
                        continue
                    else:
                        continue
